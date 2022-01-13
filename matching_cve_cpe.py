import cve_parser as cveP
import searchEngine as sEngine
import pandas as pd
from tqdm import tqdm
import json


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
        print('Engine finished and CPE-Installed softwares results dumped!')

    def match_cve_cpe(self):
        # Initialize data frame items
        sftw_names = list(self.cpe_data_dict['registry_sw'].values())
        cpe_23_names = list(self.cpe_data_dict['cpe_23_names'].values())
        sim_score = list(self.cpe_data_dict['sim_score'].values())
        asso_cve = []
        df = pd.DataFrame([sftw_names, cpe_23_names, sim_score, asso_cve]).transpose()
        df.columns = ['sftw_name', 'cpe_23', 'sim_score', 'asso_cve']

        # Matching process
        cve_gen = self.cve_funcs.get_all_cpe23_uri()
        _dict = {}
        for cpe_23, cve_id in tqdm(cve_gen, desc="Matching CPE-CVE"):
            _dict[cpe_23] = _dict.get(cpe_23, []) + [cve_id]
        df['asso_cve'] = df['cpe_23'].apply(lambda x: _dict[x] if x in _dict else [])
        self.organize_df_make_json(df)
        df.to_csv('result.csv')
        return df

    def organize_df_make_json(self, df):
        final_res = {}
        df = df.drop(df[df.sim_score < 0.5].index)
        df = df[df['asso_cve'].map(lambda d: len(d)) > 0]
        for index, row in df.iterrows():
            final_res[row['sftw_name']] = row['asso_cve']
        with open('json_final_res.json', 'w') as jf:
            json.dump(final_res, jf)



if __name__ == '__main__':
    a = MatcherCveCpe()
    print(a.match_cve_cpe())


