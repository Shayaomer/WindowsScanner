import cve_parser as cveP
import searchEngine as sEngine
import pandas as pd

class MatcherCveCpe:
    def __init__(self):
        self.cve_funcs = cveP.CveParser()   # Initialize the CVE dictionary
        self.cve_dict = self.cve_funcs.cve_collections_for_all_years

        self.search_builder = sEngine.SearchEngineBuilder() # Initialize the CPE search engine
        self.search_builder.create_models("parsed_xml.csv", "cosin")
        cpe_sw_fitter = sEngine.CpeSwFitter("parsed_xml.csv", "cosin")
        self.cpe_data_dict = cpe_sw_fitter.fit_all(5)
        print('hello')

    def match_cve_cpe(self):
        # Initialize data frame items
        sftw_names = list(self.cpe_data_dict['registry_sw'].values())
        cpe_23_names = list(self.cpe_data_dict['cpe_23_names'].values())
        sim_score = list(self.cpe_data_dict['sim_score'].values())
        asso_cve = []
        df = pd.DataFrame([sftw_names, cpe_23_names, sim_score, asso_cve]).transpose()
        df.columns = ['sftw_name', 'cpe_23', 'sim_score', 'asso_cve']







if __name__ == '__main__':
    a = MatcherCveCpe()
    print(a.match_cve_cpe())


