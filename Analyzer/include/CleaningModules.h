#pragma once

#include "Analyzer/include/AnalysisModule.h"
#include "Analyzer/include/GenEvent.h"
#include "Analyzer/include/RecoEvent.h"
#include "Analyzer/include/ObjectIdUtils.h"
#include "Analyzer/include/useful_functions.h"

class GenJetCleaner : public AnalysisModule<GenEvent> {
public:
    GenJetCleaner(const GenID<GenJet> & id_);
    virtual bool process(GenEvent & event) override;

private:
    GenID<GenJet> id;
};

class GenJetVisTauCleaner : public AnalysisModule<GenEvent> {
public:
    GenJetVisTauCleaner(const double & mindr_);
    virtual bool process(GenEvent & event) override;

private:
    double mindr;
};

class GenVisTauCleaner : public AnalysisModule<GenEvent> {
public:
    GenVisTauCleaner(const GenID<GenParticle> & id_);
    virtual bool process(GenEvent & event) override;

private:
    GenID<GenParticle> id;
};



class JetCleaner : public AnalysisModule<RecoEvent> {
public:
    JetCleaner(const ID<Jet> & id_);
    virtual bool process(RecoEvent & event) override;

private:
    ID<Jet> id;
};

class MuonCleaner : public AnalysisModule<RecoEvent> {
public:
    MuonCleaner(const ID<Muon> & id_);
    virtual bool process(RecoEvent & event) override;

private:
    ID<Muon> id;
};

class ElectronCleaner : public AnalysisModule<RecoEvent> {
public:
    ElectronCleaner(const ID<Electron> & id_);
    virtual bool process(RecoEvent & event) override;

private:
    ID<Electron> id;
};

class TauCleaner : public AnalysisModule<RecoEvent> {
public:
    TauCleaner(const ID<Tau> & id_);
    virtual bool process(RecoEvent & event) override;

private:
    ID<Tau> id;
};
