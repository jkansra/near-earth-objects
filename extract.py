"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.
The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.
The main module calls these functions with the arguments provided at the command
row, and uses the resulting collections to build an `NEODatabase`.
You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    with open(neo_csv_path, "r") as infile:
        reader = csv.reader(infile)
        next(reader)
        neos = []
        for row in reader:
            pdes = row[3]
            if row[4] == '':
                name = None 
            else:
                name = row[4]
            if row[15] == '':
                diameter = None 
            else:
                diameter = float(row[15])
            if row[7] == '' or row[7] == 'N':
                pha = False
            else:
                pha = True
            neo = NearEarthObject(
                    designation = pdes,
                    name = name,
                    diameter = diameter,
                    hazardous = pha,
                )
            neos.append(neo)
    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.
    
    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    with open(cad_json_path, 'r') as infile:
        contents = json.load(infile)
        # reader = [dict(zip(reader["fields"], data)) for data in reader["data"]]
        contentData = [data for data in contents["data"]]
        approaches = []
        for row in contentData:
            approach = CloseApproach(
                    designation=row[0],
                    time=row[3],
                    distance=float(row[4]),
                    velocity=float(row[7]),
                )
            
            approaches.append(approach)    
    return approaches