# encoding: utf-8

'''plugin.py

'''
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class ExampleThemePlugin(plugins.SingletonPlugin):
    '''An example theme plugin.

    '''
    # Declare that this class implements IConfigurer.
    plugins.implements(plugins.IConfigurer)

    def update_config(self, config):

        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        # 'templates' is the path to the templates dir, relative to this
        # plugin.py file.
        toolkit.add_template_directory(config, 'templates')
#        toolkit.add_public_directory(config, 'public')
#        toolkit.add_resource('fanstatic', 'example_theme')

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
                'example_theme_recent_datasets' : most_recent_datasets,
                'example_theme_popular_datasets' : popular_datasets,
                }
