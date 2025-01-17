#! /usr/bin/env python

import os, sys, math
from os.path import isfile, join
import subprocess
import time
import parse
from operator import itemgetter
import importlib
from utils import *
from functions import *
import json
from yaml import safe_load
from multiprocessing import Pool

import ROOT
from ROOT import gROOT, gStyle, gPad, TLegend, TFile, TCanvas, Double, TF1, TH2D, TGraph, TGraph2D, TGraphAsymmErrors, TLine,\
                 kBlack, kRed, kBlue, kAzure, kCyan, kGreen, kGreen, kYellow, kOrange, kMagenta, kViolet,\
                 kSolid, kDashed, kDotted
from math import sqrt, log, floor, ceil
from array import array

# from preferred_configurations import *
from tdrstyle_all import *
import tdrstyle_all as TDR

class YearDependentContainer():
    def __init__(self, vals={}):
        self.dict = {
            '2016': None,
            '2017': None,
            '2018': None
        }
        for key in vals.keys():
            if key in self.dict.keys():
                self.dict[key] = vals[key]
            else:
                raise AttributeError('Invalid key %s for year-dependent object.' % str(key))

    def __getitem__(self, year):
        if self.has_year(year):
            return self.dict[year]
        else:
            return None

    def has_year(self, year):
        if year in self.dict.keys():
            if self.dict[year] is not None:
                return True
        return False

    def __setitem__(self, year, value):
        if not self.has_year(year):
            self.dict = {year: value}
        else:
            raise AttributeError('Year-dependent dict already has an entry for year %s' % (str(year)))


class Sample:
    def __init__(self, type, name, group=YearDependentContainer(), minipaths=YearDependentContainer(), nanopaths=YearDependentContainer(), tuplepaths=YearDependentContainer(), xsecs=YearDependentContainer(), xmlfiles=YearDependentContainer(), nevents=YearDependentContainer()):
        self.type = type
        self.name = name
        self.group = group
        self.minipaths = minipaths
        self.nanopaths = nanopaths
        self.tuplepaths = tuplepaths
        self.xsecs = xsecs
        self.xmlfiles = xmlfiles
        self.nevents = nevents

    def get_info(self, year):
        print '--> Info on sample \'%s\' for year %s:' % (self.name, str(year))
        print '  --> type: %s' % (str(self.type))
        print '  --> name: %s' % (str(self.name))
        print '  --> group: %s' % (str(self.group[year]))
        print '  --> minipath: %s' % (str(self.minipaths[year].path))
        print '  --> nanopath: %s' % (str(self.nanopaths[year].path))
        print '  --> tuplepath: %s' % (str(self.tuplepaths[year].path))
        print '  --> xsec: %s' % (str(self.xsecs[year]))
        print '  --> xmlfile: %s' % (str(self.xmlfiles[year]))
        print '  --> nevent: %s' % (str(self.nevents[year]))

    def get_var_for_year(self, varname, year):
        if varname is 'type' or varname is 'name':
            return getattr(self, varname)
        elif varname is 'minipaths' or varname is 'nanopaths' or varname is 'tuplepaths':
            return getattr(self, varname)[year].path
        else:
            return getattr(self, varname)[year]

    def get_filedict(self, sampleinfofolder, stage, year, check_missing=False, force_update=False):
        if stage is not 'nano' and stage is not 'mini':
            raise AttributeError('Invalid stage defined. Must be \'mini\' or \'nano\'.')

        # first try to read it from the json
        filedict = self.get_filedict_from_json(sampleinfofolder=sampleinfofolder, stage=stage, year=year)
        if filedict is not False:
            if not force_update and not check_missing:
                return filedict
            else:
                pass


        # if it wasn't found, call the function to find the list, update the json, and return the list then
        if stage is 'nano':
            filelist = self.nanopaths[year].get_file_list()
        elif stage is 'mini':
            filelist = self.minipaths[year].get_file_list()

        if filedict is not False:
            if check_missing:
                if len(filedict) == len(filelist):
                    print green('  --> Sample \'%s\' has all files counted, continue.' % (self.name))
                    return filedict


        filedict = self.count_events_in_files(filelist, stage=stage)
        self.update_filedict_in_json(sampleinfofolder=sampleinfofolder, stage=stage, year=year, filedict=filedict)

        # get from json to make sure it's always ordered in the same way
        filedict = self.get_filedict_from_json(sampleinfofolder=sampleinfofolder, stage=stage, year=year)

        if filedict is not False:
            return filedict
        else:
            raise ValueError('Unable to get filedict for sample %s.' % (self.name))

    def get_filedict_from_json(self, sampleinfofolder, stage, year):
        if stage is not 'nano' and stage is not 'mini':
            raise AttributeError('Invalid stage defined. Must be \'mini\' or \'nano\'.')
        jsonname = os.path.join(sampleinfofolder, 'filelist_%s_%s.json' % (stage, year))
        dict_in_json = {}

        if not os.path.exists(jsonname):
            return False
        with open(jsonname, 'r') as j:
            dict_in_json = safe_load(j)

        if not self.name in dict_in_json.keys():
            return False
        return dict_in_json[self.name]


    def update_filedict_in_json(self, sampleinfofolder, stage, year, filedict):
        if stage is not 'nano' and stage is not 'mini':
            raise AttributeError('Invalid stage defined. Must be \'mini\' or \'nano\'.')
        jsonname = os.path.join(sampleinfofolder, 'filelist_%s_%s.json' % (stage, year))
        dict_in_json = {}
        if os.path.exists(jsonname):
            with open(jsonname, 'r') as j:
                dict_in_json = safe_load(j)

        # print dict_in_json
        dict_in_json[self.name] = filedict
        with open(jsonname, 'w') as j:
            json.dump(obj=dict_in_json, fp=j, indent=2, sort_keys=True)


    def count_events_in_files(self, filelist, stage, ncores=10, chunksize=5, maxtries=5):
        if stage is not 'nano' and stage is not 'mini':
            raise AttributeError('Invalid stage defined. Must be \'mini\' or \'nano\'.')
        print green('  --> Going to count events in %i files' % (len(filelist)))
        # commands = []
        # for i, filename in enumerate(filelist):
        #
        #     # get number of events
        #     command = 'Counter_NANOAOD %s' % (filename)
        #     commands.append((command, filename))
        # outputs = getoutput_commands_parallel(commands=commands, max_time=30, ncores=10)
        #
        # newdict = {}
        # for o in outputs:
        #     try:
        #         nevt = int(o[0].split('\n')[0])
        #         filename = o[1]
        #         newdict[filename] = nevt
        #     except Exception as e:
        #         print yellow('  --> Caught exception \'%s\'. Skip sample \'%s\'.' % (e, self.name))
        #         return False


        #################################


        pool = Pool(processes=ncores)
        result = pool.map(countEventsInFileGrid, filelist, chunksize)
        pool.terminate()
        pool.close()

        # Output the result
        newdict = {}
        failed_files = []
        for d in result:
            if d[d.keys()[0]] is None:
                failed_files.append(d.keys()[0])
            else:
                newdict.update(d)

        idx = 0
        while len(failed_files) > 0 and idx < maxtries:
            failed_files_loop = []

            pool = Pool(processes=ncores)
            result = pool.map(countEventsInFileGrid, failed_files, chunksize)
            pool.terminate()
            pool.close()

            for d in result:
                if d[d.keys()[0]] is None:
                    failed_files_loop.append(d.keys()[0])
                else:
                    newdict.update(d)
            failed_files = failed_files_loop
            idx += 1





            # pbar = tqdm(range(len(failed_files)), desc="Files counted")
            # for idx in pbar:
            #     filename = failed_files[idx]
            #     nevt = countEventsInFileGrid(absolute_filename=filename)
            #     if nevt is None:
            #         failed_files_loop.append(filename)
            #     else:
            #         newdict[filename]=nevt
            # failed_files = failed_files_loop



        #################################



        # failed_files = []
        # newdict = {}
        # pbar = tqdm(range(len(filelist)), desc="Files counted")
        # for idx in pbar:
        #     filename = filelist[idx]
        #     nevt = countEventsInFileGrid(absolute_filename=filename)
        #     if nevt is None:
        #         failed_files.append(filename)
        #     else:
        #         newdict[filename]=nevt
        #
        # idx = 0
        # keep_going = True
        # while len(failed_files) > 0 and idx < maxtries:
        #     failed_files_loop = []
        #     pbar = tqdm(range(len(failed_files)), desc="Files counted")
        #     for idx in pbar:
        #         filename = failed_files[idx]
        #         nevt = countEventsInFileGrid(absolute_filename=filename)
        #         if nevt is None:
        #             failed_files_loop.append(filename)
        #         else:
        #             newdict[filename]=nevt
        #     failed_files = failed_files_loop


        print green('  --> Successfully counted events in %i files' % (len(newdict)))
        return newdict
