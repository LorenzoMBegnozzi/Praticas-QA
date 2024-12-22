import { test, expect } from '@playwright/test';


test("Teste basico de navegaçao!", async ({ page }) => {
  await page.goto("https:/gitlab.com/"); //acessar o site
  await page.waitForTimeout(3000);   //esperar 3000ms
  await page.reload(); //recarregar pagina 
});

test("Clicando em um elemento", async ({ page }) => {
  await page.goto("https://gitlab.com/");//acessar o site
  await page.click('#onetrust-accept-btn-handler')
  await page.waitForTimeout(3000);
  
})

