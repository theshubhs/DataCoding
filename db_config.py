from configparser import ConfigParser

def read_postgre_config(filename='config.ini', section= 'postgresql'):
    """ Read database configuration file and return a dictionary object
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return: a dictionary of database parameters
    """
    
    parser = ConfigParser()
    parser.read(filename)
    # postgredb = {}
    postgredb = {}
    for section in parser.sections():
        # postgredb[section] = {}
        for key, value in parser.items(section):
            # Now try to convert back to original types if possible
            for boolean in ['True', 'False', 'None']:
                if value == boolean:
                    value = bool(boolean)

            # Try to convert to float or int
            try:
                if isinstance(value, str):
                    if '.' in value:
                        value = float(value)
                    else:
                        value = int(value)
            except ValueError:
                pass

            postgredb[key] = value

    # Now drop root section if present
    postgredb.pop('root', None)
    
    return postgredb
    # print(postgredb)

# configparser_to_dict()