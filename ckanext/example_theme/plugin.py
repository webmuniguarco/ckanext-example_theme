"""
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class Example_ThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'example_theme')
"""

# encoding: utf-8

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.common import config
from ckanext.pages.interfaces import IPagesSchema
import ckan.logic.action.get as tk

def show_most_popular_groups():

    value = config.get('ckan.example_theme.show_most_popular_groups', False)
    value = toolkit.asbool(value)
    return value


def most_popular_groups():
    '''Return a sorted list of the groups with the most datasets.'''

    # Get a list of all the site's groups from CKAN, sorted by number of
    # datasets.
    groups = toolkit.get_action('group_list')(
        data_dict={ 'all_fields': True}) #'sort': 'packages desc',

    # Truncate the list to the 10 most popular groups only.
    groups = groups[:10]

    return groups

def all_categories():
    all_categories_list = []

    category = {}
    category['text'] = "Agriculture, Food & Forests"
    category['img_src'] = "/example_theme_categories/agriculture.png"
    category['url'] = "#"
    all_categories_list.append(category)

    category = {}
    category['text'] = "Cities & Regions"
    category['img_src'] = "/example_theme_categories/cities.png"
    category['url'] = "#"
    all_categories_list.append(category)

    category = {}
    category['text'] = "Connectivity"
    category['img_src'] = "/example_theme_categories/connectivity.png"
    category['url'] = "#"
    all_categories_list.append(category)

    category = {}
    category['text'] = "Culture"
    category['img_src'] = "/example_theme_categories/culture.png"
    category['url'] = "#"
    all_categories_list.append(category)

    category = {}
    category['text'] = "Demography"
    category['img_src'] = "/example_theme_categories/demography.png"
    category['url'] = "#"
    all_categories_list.append(category)

    category = {}
    category['text'] = "Economy & Finance"
    category['img_src'] = "/example_theme_categories/economy.png"
    category['url'] = "#"
    all_categories_list.append(category)

    category = {}
    category['text'] = "Education"
    category['img_src'] = "/example_theme_categories/education.png"
    category['url'] = "#"
    all_categories_list.append(category)

    category = {}
    category['text'] = "Environment & Energy"
    category['img_src'] = "/example_theme_categories/environment.png"
    category['url'] = "#"
    all_categories_list.append(category)

    category = {}
    category['text'] = "Government & Public Sector"
    category['img_src'] = "/example_theme_categories/government.png"
    category['url'] = "#"
    all_categories_list.append(category)

    category = {}
    category['text'] = "Health"
    category['img_src'] = "/example_theme_categories/health.png"
    category['url'] = "#"
    all_categories_list.append(category)

    category = {}
    category['text'] = "Housing & Public Services"
    category['img_src'] = "/example_theme_categories/housing.png"
    category['url'] = "#"
    all_categories_list.append(category)

    category = {}
    category['text'] = "Manufactoring & Public Services"
    category['img_src'] = "/example_theme_categories/manufecturing.png"
    category['url'] = "#"
    all_categories_list.append(category)

    category = {}
    category['text'] = "Public Safety"
    category['img_src'] = "/example_theme_categories/publicsafety.png"
    category['url'] = "#"
    all_categories_list.append(category)

    category = {}
    category['text'] = "Science & Technology"
    category['img_src'] = "/example_theme_categories/science.png"
    category['url'] = "#"
    all_categories_list.append(category)

    return all_categories_list

def popular_datasets(limit=4):
    import urllib, json
    site_url = config.get('ckan.site_url', None)

    url = site_url + "/api/3/action/package_search?q=&sort=views_total+desc"
    response = urllib.urlopen(url)
    dict = json.loads(response.read())


    count = dict['result']['count']
    datasets = []
    if count < limit:
        limit = count
    for i in range(limit):
        dataset = dict['result']['results'][i]
        datasets.append(dataset)
    return datasets

def most_recent_datasets():
    pass
    datasets = toolkit.get_action('package_list')(
        data_dict={ 'all_fields': True}) #'sort': 'packages desc',

    datasets = datasets[:4]
    return datasets

class ExampleThemePlugin(plugins.SingletonPlugin):
    '''An example theme plugin.

    '''
    plugins.implements(plugins.IConfigurer)

    # Declare that this plugin will implement ITemplateHelpers.
    plugins.implements(plugins.ITemplateHelpers)

    plugins.implements(IPagesSchema)

    #IPagesSchema
    def update_pages_schema(self, schema):
        schema.update({
            'new_field': [
                toolkit.get_validator('not_empty'),
                toolkit.get_validator('boolean_validator')]
            })
        return schema
 
    def update_config(self, config):

        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource('fanstatic', 'example_theme')

    def get_helpers(self):
        '''Register the most_popular_groups() function above as a template
        helper function.

        '''
        # Template helper function names should begin with the name of the
        # extension they belong to, to avoid clashing with functions from
        # other extensions.
        return {'example_theme_most_popular_groups': most_popular_groups,
                'example_theme_show_most_popular_groups':
                show_most_popular_groups,
                'example_theme_all_categories_list': all_categories,
                'example_theme_recent_datasets' : most_recent_datasets,
                'example_theme_popular_datasets' : popular_datasets,
                }

