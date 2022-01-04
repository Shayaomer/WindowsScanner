import cve_parser as cveP
import searchEngine as sEngine
import pandas as pd
from tqdm import tqdm


class MatcherCveCpe:
    def __init__(self):
        self.cve_funcs = cveP.CveParser()   # Initialize the CVE dictionary
        self.cve_dict = self.cve_funcs.cve_collections_for_all_years
        print('Building the CPE search engine...')
        self.search_builder = sEngine.SearchEngineBuilder() # Initialize the CPE search engine
        print('Creating models...')
        self.search_builder.create_models("parsed_xml.csv", "cosin")
        print('Fitting results...')
        cpe_sw_fitter = sEngine.CpeSwFitter("parsed_xml.csv", "cosin")
        self.cpe_data_dict = cpe_sw_fitter.fit_all(1)
        print('Engine finished and CPE results dumped!')

    def match_cve_cpe(self):
        print('Matching CVE-CPE...')
        # Initialize data frame items
        sftw_names = list(self.cpe_data_dict['registry_sw'].values())
        cpe_23_names = list(self.cpe_data_dict['cpe_23_names'].values())
        sim_score = list(self.cpe_data_dict['sim_score'].values())
        asso_cve = []
        for i in range(len(sim_score)):
            asso_cve.append([])
        df = pd.DataFrame([sftw_names, cpe_23_names, sim_score, asso_cve]).transpose()
        df.columns = ['sftw_name', 'cpe_23', 'sim_score', 'asso_cve']

        # Matching process
        cve_gen = self.cve_funcs.get_all_cpe23_uri()
        for next_cve in tqdm(cve_gen):
            temp_df = df[df.cpe_23 == next_cve[0]]
            if not temp_df.empty:
                for index_temp, row_temp in temp_df.iterrows():
                    for index, row in df.loc[df['cpe_23'] == row_temp['cpe_23'], ['asso_cve']].iterrows():
                        row['asso_cve'].append(next_cve[1])
        for index, row in df.loc[:, ['asso_cve']].iterrows():
            row['asso_cve'] = list(dict.fromkeys(row['asso_cve']))
        df.to_csv('result.csv')
        return df













if __name__ == '__main__':
    a = MatcherCveCpe()
    print(a.match_cve_cpe())


