// adapted from a few different sources:
// https://medium.com/dailyjs/how-to-setup-selenium-on-node-environment-ee33023da72d

var webdriver = require('selenium-webdriver'),
    By = webdriver.By,
    until = webdriver.until;

var capabilities = {
    'browserName': 'Chrome'
}

var driver = new webdriver.Builder()
    .usingServer('http://tester:4444/wd/hub')
    .forBrowser('chrome')
    .build();

driver.get('http://www.google.com').then(function() {
    driver.findElement(webdriver.By.name('q')).sendKeys('webdriver\n').then(function() {
        driver.getTitle().then(function(title) {
            console.log(title);
            if (title == 'webdriver - Google Search') {
                console.log('Test passed');
            } else {
                console.log('Test failed');
            }
            driver.quit();
        });
    });
});
// driver.get('http://www.google.com');
// driver.findElement(webdriver.By.name('q')).sendKeys('simple programmer');
// driver.findElement(webdriver.By.name('btnG')).click();
// driver.quit();