from Sample import *
from Storage import *

# data = {
datalist = [

    ('DATA_Tau_B', Sample(
        type='DATA',
        name='DATA_Tau_B',
        group=YearDependentContainer({'2017': 'DATA_Tau'}),
        nanopaths=YearDependentContainer({'2017': Storage_DAS('/Tau/Run2017B-UL2017_02Dec2019-v1/NANOAOD')}),
        tuplepaths=YearDependentContainer({'2017': Storage_T3PSI('/store/user/areimers/UL17/Tuples_v02_NANOAOD/DATA_Tau_B')}),
        xsecs=YearDependentContainer(),
        xmlfiles=YearDependentContainer({'2017': 'datasets/UL17/Recolevel/DATA_Tau_B.xml'}),
        nevents=YearDependentContainer({'2017': 38158216})
    )),

    ('DATA_Tau_C', Sample(
        type='DATA',
        name='DATA_Tau_C',
        group=YearDependentContainer({'2017': 'DATA_Tau'}),
        nanopaths=YearDependentContainer({'2017': Storage_DAS('/Tau/Run2017C-UL2017_02Dec2019-v1/NANOAOD')}),
        tuplepaths=YearDependentContainer({'2017': Storage_T3PSI('/store/user/areimers/UL17/Tuples_v02_NANOAOD/DATA_Tau_C')}),
        xsecs=YearDependentContainer(),
        xmlfiles=YearDependentContainer({'2017': 'datasets/UL17/Recolevel/DATA_Tau_C.xml'}),
        nevents=YearDependentContainer({'2017': 55416425})
    )),

    ('DATA_Tau_D', Sample(
        type='DATA',
        name='DATA_Tau_D',
        group=YearDependentContainer({'2017': 'DATA_Tau'}),
        nanopaths=YearDependentContainer({'2017': Storage_DAS('/Tau/Run2017D-UL2017_02Dec2019-v1/NANOAOD')}),
        tuplepaths=YearDependentContainer({'2017': Storage_T3PSI('/store/user/areimers/UL17/Tuples_v02_NANOAOD/DATA_Tau_D')}),
        xsecs=YearDependentContainer(),
        xmlfiles=YearDependentContainer({'2017': 'datasets/UL17/Recolevel/DATA_Tau_D.xml'}),
        nevents=YearDependentContainer({'2017': 20530776})
    )),

    ('DATA_Tau_E', Sample(
        type='DATA',
        name='DATA_Tau_E',
        group=YearDependentContainer({'2017': 'DATA_Tau'}),
        nanopaths=YearDependentContainer({'2017': Storage_DAS('/Tau/Run2017E-UL2017_02Dec2019-v1/NANOAOD')}),
        tuplepaths=YearDependentContainer({'2017': Storage_T3PSI('/store/user/areimers/UL17/Tuples_v02_NANOAOD/DATA_Tau_E')}),
        xsecs=YearDependentContainer(),
        xmlfiles=YearDependentContainer({'2017': 'datasets/UL17/Recolevel/DATA_Tau_E.xml'}),
        nevents=YearDependentContainer({'2017': 43234212})
    )),

    ('DATA_Tau_F', Sample(
        type='DATA',
        name='DATA_Tau_F',
        group=YearDependentContainer({'2017': 'DATA_Tau'}),
        nanopaths=YearDependentContainer({'2017': Storage_DAS('/Tau/Run2017F-UL2017_02Dec2019-v1/NANOAOD')}),
        tuplepaths=YearDependentContainer({'2017': Storage_T3PSI('/store/user/areimers/UL17/Tuples_v02_NANOAOD/DATA_Tau_F')}),
        xsecs=YearDependentContainer(),
        xmlfiles=YearDependentContainer({'2017': 'datasets/UL17/Recolevel/DATA_Tau_F.xml'}),
        nevents=YearDependentContainer({'2017': 88505129})
    )),

    ('DATA_SingleMuon_B', Sample(
        type='DATA',
        name='DATA_SingleMuon_B',
        group=YearDependentContainer({'2017': 'DATA_SingleMuon'}),
        nanopaths=YearDependentContainer({'2017': Storage_DAS('/SingleMuon/Run2017B-UL2017_02Dec2019-v1/NANOAOD')}),
        tuplepaths=YearDependentContainer({'2017': Storage_T3PSI('/store/user/areimers/UL17/Tuples_v02_NANOAOD/DATA_SingleMuon_B')}),
        xsecs=YearDependentContainer(),
        xmlfiles=YearDependentContainer({'2017': 'datasets/UL17/Recolevel/DATA_SingleMuon_B.xml'}),
        nevents=YearDependentContainer({'2017': 136300266.0})
    )),

    ('DATA_SingleMuon_C', Sample(
        type='DATA',
        name='DATA_SingleMuon_C',
        group=YearDependentContainer({'2017': 'DATA_SingleMuon'}),
        nanopaths=YearDependentContainer({'2017': Storage_DAS('/SingleMuon/Run2017C-UL2017_02Dec2019-v1/NANOAOD')}),
        tuplepaths=YearDependentContainer({'2017': Storage_T3PSI('/store/user/areimers/UL17/Tuples_v02_NANOAOD/DATA_SingleMuon_C')}),
        xsecs=YearDependentContainer(),
        xmlfiles=YearDependentContainer({'2017': 'datasets/UL17/Recolevel/DATA_SingleMuon_C.xml'}),
        nevents=YearDependentContainer({'2017': 165652756.0})
    )),

    ('DATA_SingleMuon_D', Sample(
        type='DATA',
        name='DATA_SingleMuon_D',
        group=YearDependentContainer({'2017': 'DATA_SingleMuon'}),
        nanopaths=YearDependentContainer({'2017': Storage_DAS('/SingleMuon/Run2017D-UL2017_02Dec2019-v1/NANOAOD')}),
        tuplepaths=YearDependentContainer({'2017': Storage_T3PSI('/store/user/areimers/UL17/Tuples_v02_NANOAOD/DATA_SingleMuon_D')}),
        xsecs=YearDependentContainer(),
        xmlfiles=YearDependentContainer({'2017': 'datasets/UL17/Recolevel/DATA_SingleMuon_D.xml'}),
        nevents=YearDependentContainer()
    )),

    ('DATA_SingleMuon_E', Sample(
        type='DATA',
        name='DATA_SingleMuon_E',
        group=YearDependentContainer({'2017': 'DATA_SingleMuon'}),
        nanopaths=YearDependentContainer({'2017': Storage_DAS('/SingleMuon/Run2017E-UL2017_02Dec2019-v1/NANOAOD')}),
        tuplepaths=YearDependentContainer({'2017': Storage_T3PSI('/store/user/areimers/UL17/Tuples_v02_NANOAOD/DATA_SingleMuon_E')}),
        xsecs=YearDependentContainer(),
        xmlfiles=YearDependentContainer({'2017': 'datasets/UL17/Recolevel/DATA_SingleMuon_E.xml'}),
        nevents=YearDependentContainer({'2017': 154567348.0})
    )),

    ('DATA_SingleMuon_F', Sample(
        type='DATA',
        name='DATA_SingleMuon_F',
        group=YearDependentContainer({'2017': 'DATA_SingleMuon'}),
        nanopaths=YearDependentContainer({'2017': Storage_DAS('/SingleMuon/Run2017F-UL2017_02Dec2019-v1/NANOAOD')}),
        tuplepaths=YearDependentContainer({'2017': Storage_T3PSI('/store/user/areimers/UL17/Tuples_v02_NANOAOD/DATA_SingleMuon_F')}),
        xsecs=YearDependentContainer(),
        xmlfiles=YearDependentContainer({'2017': 'datasets/UL17/Recolevel/DATA_SingleMuon_F.xml'}),
        nevents=YearDependentContainer({'2017': 242140980.0})
    )),

    ('DATA_SingleElectron_B', Sample(
        type='DATA',
        name='DATA_SingleElectron_B',
        group=YearDependentContainer({'2017': 'DATA_SingleElectron'}),
        nanopaths=YearDependentContainer({'2017': Storage_DAS('/SingleElectron/Run2017B-UL2017_02Dec2019-v1/NANOAOD')}),
        tuplepaths=YearDependentContainer({'2017': Storage_T3PSI('/store/user/areimers/UL17/Tuples_v02_NANOAOD/DATA_SingleElectron_B')}),
        xsecs=YearDependentContainer(),
        xmlfiles=YearDependentContainer({'2017': 'datasets/UL17/Recolevel/DATA_SingleElectron_B.xml'}),
        nevents=YearDependentContainer({'2017': 60537490.0})
    )),

    ('DATA_SingleElectron_C', Sample(
        type='DATA',
        name='DATA_SingleElectron_C',
        group=YearDependentContainer({'2017': 'DATA_SingleElectron'}),
        nanopaths=YearDependentContainer({'2017': Storage_DAS('/SingleElectron/Run2017C-UL2017_02Dec2019-v1/NANOAOD')}),
        tuplepaths=YearDependentContainer({'2017': Storage_T3PSI('/store/user/areimers/UL17/Tuples_v02_NANOAOD/DATA_SingleElectron_C')}),
        xsecs=YearDependentContainer(),
        xmlfiles=YearDependentContainer({'2017': 'datasets/UL17/Recolevel/DATA_SingleElectron_C.xml'}),
        nevents=YearDependentContainer()
    )),

    ('DATA_SingleElectron_D', Sample(
        type='DATA',
        name='DATA_SingleElectron_D',
        group=YearDependentContainer({'2017': 'DATA_SingleElectron'}),
        nanopaths=YearDependentContainer({'2017': Storage_DAS('/SingleElectron/Run2017D-UL2017_02Dec2019-v1/NANOAOD')}),
        tuplepaths=YearDependentContainer({'2017': Storage_T3PSI('/store/user/areimers/UL17/Tuples_v02_NANOAOD/DATA_SingleElectron_D')}),
        xsecs=YearDependentContainer(),
        xmlfiles=YearDependentContainer({'2017': 'datasets/UL17/Recolevel/DATA_SingleElectron_D.xml'}),
        nevents=YearDependentContainer()
    )),

    ('DATA_SingleElectron_E', Sample(
        type='DATA',
        name='DATA_SingleElectron_E',
        group=YearDependentContainer({'2017': 'DATA_SingleElectron'}),
        nanopaths=YearDependentContainer({'2017': Storage_DAS('/SingleElectron/Run2017E-UL2017_02Dec2019-v1/NANOAOD')}),
        tuplepaths=YearDependentContainer({'2017': Storage_T3PSI('/store/user/areimers/UL17/Tuples_v02_NANOAOD/DATA_SingleElectron_E')}),
        xsecs=YearDependentContainer(),
        xmlfiles=YearDependentContainer({'2017': 'datasets/UL17/Recolevel/DATA_SingleElectron_E.xml'}),
        nevents=YearDependentContainer()
    )),

    ('DATA_SingleElectron_F', Sample(
        type='DATA',
        name='DATA_SingleElectron_F',
        group=YearDependentContainer({'2017': 'DATA_SingleElectron'}),
        nanopaths=YearDependentContainer({'2017': Storage_DAS('/SingleElectron/Run2017F-UL2017_02Dec2019-v1/NANOAOD')}),
        tuplepaths=YearDependentContainer({'2017': Storage_T3PSI('/store/user/areimers/UL17/Tuples_v02_NANOAOD/DATA_SingleElectron_F')}),
        xsecs=YearDependentContainer(),
        xmlfiles=YearDependentContainer({'2017': 'datasets/UL17/Recolevel/DATA_SingleElectron_F.xml'}),
        nevents=YearDependentContainer()
    ))

]
# }
