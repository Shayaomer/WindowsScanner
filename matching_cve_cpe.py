import cve_parser as cveP
import searchEngine as sEngine

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
        yield 0

if __name__ == '__main__':
    a = MatcherCveCpe()
    print(a.match_cve_cpe())


