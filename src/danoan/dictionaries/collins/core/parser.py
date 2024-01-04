from dataclasses import dataclass
from typing import List

from bs4 import BeautifulSoup


# -------------------- Data classes --------------------
@dataclass
class GetBestMatchingResponse:
    error: bool
    entry_id: str = ""


@dataclass
class GetEntryResponse:
    error: bool
    list_of_definitions: List[str] = []


# -------------------- XML Parser --------------------
def parse_get_best_matching(
    get_best_matching_xml_response: str,
) -> GetBestMatchingResponse:
    xml_parsed_response = BeautifulSoup(get_best_matching_xml_response, "xml")

    if xml_parsed_response.find("error") is not None:
        return GetBestMatchingResponse(True)
    else:
        entry_id = xml_parsed_response.find("entryId").getText()
        return GetBestMatchingResponse(False, entry_id)


def parse_get_entry(get_entry_xml_response: str) -> GetEntryResponse:
    xml_parsed_response = BeautifulSoup(get_entry_xml_response, "xml")

    if xml_parsed_response.find("error") is not None:
        return GetEntryResponse(True)

    html_content = xml_parsed_response.find("entryContent").getText()
    html_parsed = BeautifulSoup(html_content, "html.parser")

    def is_definition(tag):
        return tag.name == "span" and tag.has_attr("class") and "def" in tag["class"]

    list_of_definitions = [tag.getText() for tag in html_parsed.find_all(is_definition)]
    return GetEntryResponse(False, list_of_definitions)
