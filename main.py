import os

from installed_softwares import InstalledSoftware
from xmlParser import CpeXmlParser
from matching_cve_cpe import MatcherCveCpe
from download_db import DownloadDb
import download_db

def execute():
    if not os.path.isfile('official-cpe-dictionary_v2.3.xml'):
        print("Downloading CVE data...")
        a = DownloadDb()
        print("Downloading CPE data...")
        download_db.download_file()
        download_db.unzip_file('official-cpe-dictionary_v2.3.xml.zip', directory_to_extract=None)

    if not os.path.isfile("registry_data.json"):
        print('Getting installed softwares...')
        i_s = InstalledSoftware()
        i_s.dump_software_lst_to_json(["Publisher", 'DisplayVersion', 'DisplayName'])

    if not os.path.isfile("parsed_xml.csv"):
        print('Parsing the CPE data...')
        b = CpeXmlParser('official-cpe-dictionary_v2.3.xml')
        b.csv_creator('official-cpe-dictionary_v2.3.xml')
    print('Start the CVE-CPE matching process...')
    c = MatcherCveCpe()
    print(c.match_cve_cpe())


if __name__ == '__main__':
    execute()