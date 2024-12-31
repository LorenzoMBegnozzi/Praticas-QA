import { test, expect } from '@playwright/test';


test("Teste basico de navegaçao!", async ({ page }) => {
    await page.goto("https:/gitlab.com/"); //acessar o site
    await page.waitForTimeout(3000);   //esperar 3000ms
    await page.reload(); //recarregar pagina 
});

test("Clicando em um elemento", async ({ page }) => {
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
    console.log("Sign in marcado com sucesso!");

})

test("GitHub", async ({ page }) => {
    await page.goto("https://github.com/");

    await page.getByRole('link', { name: 'Sign in' }).click();
    console.log("Sign in clicado");

    await page.locator('[id="login_field"]').fill('Login-Teste');
    await page.locator('[id="password"]').fill('Senha-Teste');

    await page.click('[data-signin-label="Sign in"]');
    console.log("Clicado em login");

    await page.waitForTimeout(1000);   //esperar 1000ms

    // Verificar se o alerta de erro de senha aparece
    const errorAlert = await page.locator('div[role="alert"]').isVisible();

    if (errorAlert) {
        console.log("Erro de login detectado! Direcionando para criar uma conta!");

        await page.click('[data-ga-click="Sign in, switch to sign up"]')
        
    } else {
        console.log("Login bem-sucedido ou sem erro.");
    }


    await page.locator('[id="email"]').fill('teste@teste.com')
    await page.locator('[id="password"]').fill('teste-senha')
    await page.locator('[id="login"]').fill('Nome-Teste')

    await page.waitForTimeout(1000);   //esperar 1000ms
});
