import { test, expect } from '@playwright/test';


test("Teste basico de navegaçao!", async ({ page }) => {
    await page.goto("https:/gitlab.com/"); 
    await page.waitForTimeout(3000);   
    await page.reload(); 
});

test("Clicando em um elemento", async ({ page }) => {
    await page.goto("https://gitlab.com/");
    await page.click('#onetrust-accept-btn-handler') //clica no aceitar cookies
    await page.locator('#be-navigation-desktop').getByRole('link', { name: 'Get free trial' }).click(); 
    await page.locator('[data-testid="new-user-first-name-field"]').fill('Pedro1')
    await page.locator('[data-testid="new-user-last-name-field"]').fill('Henrique')
})

test("usando varios locators", async ({ page }) => {
    await page.goto("https://gitlab.com/");
    await page.click('#onetrust-accept-btn-handler')
    await page.getByRole('link', { name: 'Sign in' }).click()
    console.log("Sign in marcado com sucesso!");

})

