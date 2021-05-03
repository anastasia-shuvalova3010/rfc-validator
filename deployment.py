from malapi import deploy
import logging
from owlready2 import *
from validator.onto import onto, load_ontology, load_rules
from datetime import date


def get_ontology():
    return load_ontology('file://onto/rfc_ontology_v3.owl')


def get_rules():
    rules = load_rules('rules/rules.txt', 'rules/background_rules.txt')
    return rules


class VeRu:

    def __init__(self):
        self.rules = get_rules()
        self.ontology = get_ontology()

    @deploy
    def validate(self, attrs):

        # RFC properties
        try:
            type = attrs["type"]
            start_date = attrs['start_date']
            end_date = attrs["end_date"]
            impacted_country = attrs["impacted_country"]
            assigned_group = attrs["assigned_group"]
            has_category = attrs["category"]
            has_ci = attrs["impacted_ci"]
            has_impacted_bu = attrs["impacted_bu"]
            has_impacted_service = attrs["impacted_service"]
            has_number = attrs["number"]
            has_outage_end_date = attrs["outage_end"]
            has_outage_start_date = attrs["outage_start"]
            has_potentially_impacted_service = attrs["potentially_impacted"]
            has_state = attrs["state"]
            backout_planned = attrs["backout_planned"]
            requires_outage_of = attrs["outage_service"]

            rfc_list = [type,
                        start_date,
                        end_date,
                        impacted_country,
                        assigned_group,
                        has_category,
                        has_ci,
                        has_impacted_bu,
                        has_impacted_service,
                        has_number,
                        has_outage_end_date,
                        has_outage_start_date,
                        has_potentially_impacted_service,
                        has_state,
                        backout_planned,
                        requires_outage_of]

        except KeyError:
            logging.warning("Missing RFC attributes")

        # Business Unit properties
        try:
            bu_name = attrs["bu_name"]

            bu_list = [bu_name]

        except KeyError:
            logging.warning("Missing BU attributes")

        # Control Item properties
        try:
            ci_has_name = attrs["ci_name"]
            ci_has_category = attrs["ci_category"]
            ci_has_state = attrs["ci_state"]
            related_service = attrs["ci_service"]
            ci_managed_by = attrs["ci_managed_by"]

            ci_list = [ci_has_name, ci_has_category, ci_has_state, related_service, ci_managed_by]

        except KeyError:
            logging.warning("Missing CI attributes")

        # Service properties
        try:
            service_has_category = attrs["service_category"]
            service_has_name = attrs["service_name"]
            service_has_state = attrs["service_state"]
            related_ci = attrs["related_ci"]
            service_managed_by = attrs["service_managed_by"]

            service_list = [service_has_category, service_has_name, service_has_state, related_ci, service_managed_by]

        except KeyError:
            logging.warning("Missing Service attributes")

        # Country properties
        try:

            country_region = attrs["region"]

            country_list = [country_region]

        except KeyError:
            logging.warning("Missing Country attributes")

        result = onto(self.rules, rfc_list, bu_list, ci_list, service_list, country_list)
        return result
