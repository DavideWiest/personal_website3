from .base import openContentFile
import math

def categoriesByReferenceCountWithBrightness(cutoff):
    return listTagProjectsByReferenceCountAndBrightness("c", cutoff)

def technologiesByReferenceCountWithBrightness(cutoff):
    return listTagProjectsByReferenceCountAndBrightness("t", cutoff)

def listTagProjectsByReferenceCountAndBrightness(k, cutoff):
    projects_content = openContentFile("projects_content.json", "projects")

    technologyDict = {}
    for _, project in projects_content.items():
        for technology in project.get(k, []):
            technologyDict[technology] = technologyDict.get(technology, 0) + 1

    sortedDict = sortDict(technologyDict, cutoff)
    colorDict = getBlueColorFromValues(sortedDict)

    return mergeDictsWithValueList(sortedDict, colorDict)

def sortDict(dict, cutoff):
    sorted_items = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    sorted_items = sorted_items[:cutoff] if cutoff != None else sorted_items

    return {item: count for item, count in sorted_items}

def getBlueColorFromValues(data):
  max_value = max(data.values())
  color_dict = {}
  for key, value in data.items():
    normalized_value = (value / max_value) ** (1/1.5)
    blue_value = int(normalized_value * 255)
    red_value = int(normalized_value * 80)
    green_value = int(normalized_value * 50)
    color_dict[key] = f"rgba({red_value}, {green_value}, {blue_value}, {normalized_value})"
  return color_dict

def mergeDictsWithValueList(dict1, dict2):
    return {key: [dict1[key], dict2[key]] for key in dict1}
