# VSenseBox - Python toolbox for visual sensing
# GNU General Public License v3 or later (GPLv3+)
# Copyright (C) 2024 UMONS-Numediart


import os
import yaml
from yaml.loader import SafeLoader

this_dir = os.path.dirname(__file__).replace(os.sep, '/')
data_yaml = os.path.join(this_dir, "data.yaml")
selector_yaml = os.path.join(this_dir, "selector.yaml")

class DataManager(object):

    def __init__(self, data_yaml=data_yaml):
        """Read and load data from :obj:`data_yaml`.

        Parameters
        ----------
        data_yaml : str
            A YAML file of data.yaml.
        """
        with open(data_yaml) as data:
            self.raw_data = yaml.load_all(data, Loader=SafeLoader)
            self.data_list = []
            for raw_d in list(self.raw_data):
                self.data_list.append(raw_d)
    
    def get_selected_data(self, selector_yaml=selector_yaml):
        """Get the selected data.

        Parameters
        ----------
        selector_yaml : str
            A YAML file of selector.yaml.

        Returns
        -------
        str
            Package name, parameter :obj:`name` for :func:`setup()`.
        str
            Version string of the data/package, 
            parameter :obj:`version` for :func:`setup()`.
        list
            List of the included directy of the data/package, 
            parameter :obj:`packages` for :func:`setup()`.
        dict
            Dictionary of the included file of the data/package, 
            parameter :obj:`package_data` for :func:`setup()`.
        """
        
        pkg_name = "vsensebox-data-"
        version = ""
        packages = []
        package_data = {}

        with open(selector_yaml) as selector:
            self.selector_dict = yaml.load(selector, Loader=SafeLoader)
        
        for d in self.data_list:
            if d['name'].lower() == self.selector_dict['name'].lower():
                pkg_name += d['pkg_suffix']
                version = str(d['version'])
                packages = d['data_paths']
                for p in packages:
                    package_data.update({p: ["*"]})
                break
        
        return pkg_name, version, packages, package_data
