import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://gtecapp.enterprisetrn.corp/GTeC/LoginKeyCloak.asp?varUsuario=eyvesp&varDominio=Visanet&strLogin=POST")
    page.get_by_role("button", name="Avançadas").click()
    page.get_by_role("link", name="Ir para gtecapp.enterprisetrn").click()
    page.locator("frame[name=\"fraToc\"]").content_frame.get_by_text("Relatórios").click()
    page.locator("frame[name=\"fraToc\"]").content_frame.get_by_role("link", name="Prest. Chamados Técnicos").click()
    page.locator("frame[name=\"fraTopic\"]").content_frame.locator("#DtBaixaSistema_Begin_txtData").click()
    page.locator("frame[name=\"fraTopic\"]").content_frame.get_by_title("quarta-feira, 8 de outubro de").click()
    page.locator("frame[name=\"fraTopic\"]").content_frame.locator("#DtBaixaSistema_End_txtData").click()
    page.locator("frame[name=\"fraTopic\"]").content_frame.locator("#DtBaixaSistema_End_txtData_CalendarExtender_day_2_2").click()
    page.locator("frame[name=\"fraTopic\"]").content_frame.locator("#lstEvento").select_option("-1")
    page.locator("frame[name=\"fraTopic\"]").content_frame.locator("#upnEvento").click()
    page.locator("frame[name=\"fraTopic\"]").content_frame.locator("#lstEvento").select_option("1008")
    page.locator("frame[name=\"fraTopic\"]").content_frame.locator("#lstEvento").select_option("-1")
    page.locator("frame[name=\"fraTopic\"]").content_frame.locator("#upnEvento").click()
    page.locator("frame[name=\"fraTopic\"]").content_frame.locator("#lstEvento").select_option("1008")
    page.locator("frame[name=\"fraTopic\"]").content_frame.locator("#lstEvento").select_option("-1")
    page.locator("frame[name=\"fraTopic\"]").content_frame.locator("#lstPendBaixado").select_option("1")
    page.locator("frame[name=\"fraTopic\"]").content_frame.locator("#lstBitEnviado").select_option("1")
    page.locator("frame[name=\"fraTopic\"]").content_frame.get_by_role("radio", name="Salvar em CSV CSV").check()
    with page.expect_download() as download_info:
        page.locator("frame[name=\"fraTopic\"]").content_frame.get_by_role("button", name="OK").click()
    download = download_info.value

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
