import validator.onto
from owlready2 import *
from datetime import datetime, date
import json


def test_load_ontology():
    ontology_path = "onto/rfc_ontology_v3.owl"
    ontology = validator.onto.load_ontology(ontology_path)
    n_entities = len(list(ontology.classes()))
    print(n_entities)

    assert n_entities == 62, "Number of entities is not correct"


def test_load_rules():
    rules = validator.onto.load_rules('tests/test_rules.txt')
    n_rules = len(rules)
    assert n_rules == 3, "Rules loading failed"


def test_validate_rfc():
    start_date = '2020-01-01 04:12:42'
    outage_start_date = '2020-01-01 04:12:42'
    end_date = '2020-01-02 04:12:42'
    outage_end_date = '2020-01-05 04:12:42'

    rfc_attrs = ["Minor",
                 start_date,
                 end_date,
                 "Norway",
                 "SAO",
                 "Documentation",
                 "Ci",
                 "DSC",
                 "Service",
                 "1",
                 outage_start_date,
                 outage_end_date,
                 "Service",
                 "New",
                 "no",
                 "Service"]

    bu_attrs = ["ITS"]

    # Control Item properties

    ci_attrs = ["ci_name",
                "ci_has_category",
                "ci_has_state",
                "related_service",
                "ci_managed_by"]

    # Service properties

    service_attrs = ["service_has_category",
                     "service_has_name",
                     "service_has_state",
                     "related_ci",
                     "service_managed_by"]

    # Country properties

    country_attrs = ["country_region"]

    rules = validator.onto.load_rules('tests/test_rules.txt')

    result = validator.onto.onto(rules,
                                 rfc_attrs=rfc_attrs,
                                 bu_attrs=bu_attrs,
                                 ci_attrs=ci_attrs,
                                 service_attrs=service_attrs,
                                 country_attrs=country_attrs)

    return result


if __name__ == "__main__":
    test_load_rules()
    test_load_ontology()
    print(test_validate_rfc())
