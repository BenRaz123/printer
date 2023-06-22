# Imports

import sys
import os
from pyppeteer import launch
import asyncio


async def main():
    try:
        input = sys.argv[1]
    except:
        print("Please give an input file")
        sys.exit(1)
    try:
        dont_print = bool(sys.argv[3])
    except:
        dont_print = False

    pdf_path = f"{input.split('.')[0]}.pdf"

    # Creating the html file

    try:
        os.system(
            f"/opt/homebrew/bin/highlight -i {input} -o __TMP__.html -O html -k 'JetBrainsMono Nerd Font' -K 12 -l --inline-css -T {input} -W"
        )
    except:
        print("Highlighting did not work!")

    # Converting it to PDF

    browser = await launch()
    page = await browser.newPage()
    await page.goto(f"file://{os.getcwd()}/__TMP__.html")
    await page.pdf(path=pdf_path)
    await browser.close()
    print("Success!")

    # Printing the PDF

    os.remove("__TMP__.html")
    if dont_print:
        sys.exit(0)

    try:
        os.system(f"lp {pdf_path}")
    except:
        print("lp Failed!")

    os.remove(pdf_path)


asyncio.run(main())
