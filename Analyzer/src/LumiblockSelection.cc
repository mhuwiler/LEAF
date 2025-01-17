#include "Analyzer/include/LumiblockSelection.h"

#include "TFile.h"
#include "TTree.h"

using namespace std;


LumiblockSelection::LumiblockSelection(const Config & cfg){

  TString macropath = (TString)getenv("ANALYZERPATH"); // set up by setup.sh
  TString dir = (TString) cfg.get("LumiblockFile"); // relative path starting from $ANALYZERPATH
  TString infilename = macropath + "/" + dir;
  std::unique_ptr<TFile> file(TFile::Open(infilename, "READ"));

  TTree* tree = (TTree*)file->Get("LumiTree");
  if(!tree){
    throw runtime_error("In LumiblockSelection(): Did not find TTree 'LumiTree' in file '" + infilename + "'");
  }

  // only fetch branches we really need:
  TBranch * brun     = tree->GetBranch("run");
  TBranch * blb_low  = tree->GetBranch("lb_low");
  TBranch * blb_high = tree->GetBranch("lb_high");
  unsigned int run = -1;
  pair<unsigned int, unsigned int> lbs = make_pair(-1, -1);
  brun    ->SetAddress(&run);
  blb_low ->SetAddress(&lbs.first);
  blb_high->SetAddress(&lbs.second);

  for(int i=0; i<tree->GetEntries(); i++){
    tree->GetEntry(i);
    runs_and_lbs[run].emplace_back(make_pair(lbs.first, lbs.second));
  }

}

bool LumiblockSelection::passes(RecoEvent & event){
  if(!event.is_data) return true;

  // check if lumi map contains runnr.
  map<unsigned int, vector<pair<unsigned int, unsigned int>>>::iterator it = runs_and_lbs.find(event.run);
  if(it != runs_and_lbs.end()){
    for (const auto [lb_low, lb_high] : runs_and_lbs[event.run]){
      if(event.lumiblock >= lb_low && event.lumiblock <= lb_high){
        return true;
      }
    }
  }
  return false;
}
