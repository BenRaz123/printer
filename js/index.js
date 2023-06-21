import puppeteer from 'puppeteer';

(async () => {
const browser = await puppeteer.launch({headless: 'new'});  
  const page = await browser.newPage();

  await page.goto('file:///Users/ben/printer/shell/hello.html');

  await page.setViewport({width: 1080, height: 1024});

  await page.emulateMediaType('screen');

  await page.pdf({
	path: "out.pdf",
	  margin: "minimum"
  });

  console.log('done!');

})();
