import { test, expect } from '@playwright/test';


test.skip("Teste basico de navegaçao!", async ({ page }) => {
  await page.goto("https:/gitlab.com/"); //acessar o site
  await page.waitForTimeout(3000);   //esperar 3000ms
  await page.reload(); //recarregar pagina 
});

test.skip("Clicando em um elemento", async ({ page }) => {
  await page.goto("https://gitlab.com/");//acessar o site
  await page.click('#onetrust-accept-btn-handler') //clica no aceitar cookies
  await page.locator('#be-navigation-desktop').getByRole('link', { name: 'Get free trial' }).click(); /*procuta a barra o cabeçalho, e depoois 
  procura um link, e nesse link tem escrito "Get free trial"*/
  await page.locator('[data-testid="new-user-first-name-field"]').fill('Pedro1')
  await page.locator('[data-testid="new-user-last-name-field"]').fill('Henrique')
})

test("usando varios locators", async ({ page }) => {
  await page.goto("https://gitlab.com/");
  await page.click('#onetrust-accept-btn-handler')
  await page.getByRole('link', { name: 'Sign in' }).click()
  await page.waitForTimeout(3000);   //esperar 3000ms

})