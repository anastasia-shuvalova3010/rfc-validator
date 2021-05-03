from owlready2 import *
import json
import os
import logging
import datetime
from datetime import datetime, date


def load_ontology(path):
    """
    The function loads the ontology using the build-in get_ontology() function of Owlready2
    :param path: path to the ontology/ontology IRI
    :return: ontology (ontology)
    """
    ontology = get_ontology(path).load()  # "file://../onto/rdf-RFC-ontology.owl"
    return ontology


def load_rules(*args):
    """
    The function loads the SWRL rules from text files
    :param args: pathes to the files containing the rules (list)
    :return: rules (list)
    """
    rules = []
    for rules_path in args:
        with open(rules_path) as rules_file:
            for cnt, line in enumerate(rules_file):
                if line is not None:
                    rules.append(line)
    return rules


def onto(rules, rfc_attrs, bu_attrs, ci_attrs, service_attrs, country_attrs):

    """
    The function enables the HermiT reasoner
    :param rules: list of SWRL rules
    :param rfc_attrs: list of RFC attributes
    :param bu_attrs: list of Business Unit attributes
    :param ci_attrs: list of Control Item attributes
    :param service_attrs: list of Service attributes
    :param country_attrs: list of Country attributes
    :return: validation result
    """

    ontology = load_ontology("file://onto/rfc_ontology_v3.owl")

    with ontology:

        class RFC(Thing):
            pass

        class MinorRFC(RFC):
            pass

        class SignificantRFC(RFC):
            pass

        class MajorRFC(RFC):
            pass

        class CorrectRFC(RFC):
            pass

        class IncorrectLeadTimeRFC(RFC):
            pass

        class ApprovedRFC(RFC):
            pass

        class ClosedRFC(RFC):
            pass

        class RejectedRFC(RFC):
            pass

        class Task(Thing):
            pass

        class CI(Thing):
            pass

        class has_ci(RFC >> str, FunctionalProperty):
            pass

        class BuildTask(Task):
            pass

        class TestTask(Task):
            pass

        class PIR(TestTask):
            pass

        class has_test_task(RFC >> str, FunctionalProperty):
            pass

        class impacts_ITS(RFC >> str, FunctionalProperty):
            pass

        class impacts_Data_Center(RFC >> str, FunctionalProperty):
            pass

        class has_pir_assigned(RFC >> str, FunctionalProperty):
            pass

        class Service(Thing):
            pass

        class Business_Unit(Thing):
            pass

        class Impacted_BU(Business_Unit):
            pass

        class Impacted_Service(Service):
            pass

        class Country(Thing):
            pass

        class Impacted_Country(Country):
            pass

        class Group(Thing):
            pass

        class has_assigned_group(RFC >> str, FunctionalProperty):
            pass

        class assigned_to_GCM(RFC >> str):
            pass

        class Global_Change_Management(Group):
            pass

        class Data_Center(Country):
            pass

        class managed_by(Thing >> str, FunctionalProperty):
            pass

        class has_outage_end_date(RFC >> str, FunctionalProperty):
            pass

        class has_outage_start_date(RFC >> str, FunctionalProperty):
            pass

        class Normal_Country(Country):
            pass

        class has_type(RFC >> str, FunctionalProperty):
            pass

        class has_code(Impacted_Country >> str, FunctionalProperty):
            pass

        class has_region(Impacted_Country >> str, FunctionalProperty):
            pass

        class has_notification(RFC >> str):
            pass

        class BackoutRequiredRFC(RFC):
            pass

        class backout_planned(RFC >> str, FunctionalProperty):
            pass

        class IncorrectRFC(RFC):
            pass

        class CorrectRFC(RFC):
            pass

        class has_tag(RFC >> str, FunctionalProperty):
            pass

        class has_impacted_bu(RFC >> str, FunctionalProperty):
            pass

        class has_impacted_country(RFC >> str, FunctionalProperty):
            pass

        class has_impacted_service(RFC >> str, FunctionalProperty):
            pass

        class has_potentially_impacted_service(RFC >> str, FunctionalProperty):
            pass

        class has_start_date(RFC >> str, FunctionalProperty):
            pass

        class has_end_date(RFC >> str, FunctionalProperty):
            pass

        class has_number(RFC >> str, FunctionalProperty):
            pass

        class lead_time(RFC >> int, FunctionalProperty):
            pass

        class requires_outage_of(RFC >> str, FunctionalProperty):
            pass

        class has_lead_time_threshold(RFC >> int, FunctionalProperty):
            pass

        class Category(Thing):
            pass

        class NoBackoutRequiredRFC(RFC):
            pass

        class ITS(Business_Unit):
            pass

        class has_name(Thing >> str, FunctionalProperty):
            pass

        class has_region(Country >> str, FunctionalProperty):
            pass

        class SuspendedRFC(RFC):
            pass

        class Documentation(Category):
            pass

        class Tracing_ticket(Category):
            pass

        class has_category(Thing >> str, FunctionalProperty):
            pass

        class related_service(CI >> str, FunctionalProperty):
            pass

        class has_state(Thing >> str, FunctionalProperty):
            pass

        class related_ci(Service >> str, FunctionalProperty):
            pass

        class has_warning(RFC >> str, FunctionalProperty):
            pass

        rules = rules
        for rule in rules:
            imp_rule = Imp()
            imp_rule.set_as_rule(f"""{rule}""")

    ontology.save(file="./onto/rfc_ontology.owl", format="rdfxml")

    start_date = rfc_attrs[1]
    end_date = rfc_attrs[2]

    business_unit = Business_Unit(has_name=bu_attrs[0])

    control_item = CI(has_name=ci_attrs[0],
                      has_category=ci_attrs[1],
                      has_state=ci_attrs[2],
                      related_service=ci_attrs[3],
                      managed_by=ci_attrs[4])

    service = Service(has_category=service_attrs[1],
                      has_name=service_attrs[0],
                      has_state=service_attrs[2],
                      related_ci=service_attrs[3],
                      managed_by=service_attrs[4])

    country = Country(has_region=country_attrs[0])

    rfc = RFC(has_type=rfc_attrs[0],
              has_start_date=rfc_attrs[1],
              has_end_date=rfc_attrs[2],
              has_impacted_country=rfc_attrs[3],
              has_assiged_group=rfc_attrs[4],
              has_category=rfc_attrs[5],
              has_ci=rfc_attrs[6],
              has_impacted_bu=rfc_attrs[7],
              has_impacted_service=rfc_attrs[8],
              has_number=rfc_attrs[9],
              has_outage_end_date=rfc_attrs[11],
              has_outage_start_date=rfc_attrs[10],
              has_potentially_impacted_service=rfc_attrs[12],
              has_state=rfc_attrs[13],
              backout_planned=rfc_attrs[14],
              requires_outage_of=rfc_attrs[15]
              )

    start = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
    end = datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S')

    delta = end - start
    rfc.lead_time = int(delta.days)
    try:
        sync_reasoner_pellet(infer_property_values=True, infer_data_property_values=True)

    except OwlReadyInconsistentOntologyError:
        logging.error("Inconsistent ontology! Validation failed")
        return 1

    notification = []
    warning = []

    if rfc.has_notification:
        notification.append(rfc.has_notification)

    if rfc.has_warning:
        warning.append(rfc.has_warning)

    result = []

    if notification:
        result.append(notification)

        if warning:
            result.append(warning)

    rfc.has_tag = "Correct"
    return result

