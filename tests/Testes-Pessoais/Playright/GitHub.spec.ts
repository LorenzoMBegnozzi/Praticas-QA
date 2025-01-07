import test from "@playwright/test";

test("GitHub", async ({ page }) => {
    await page.goto("https://github.com/");

    await page.getByRole('link', { name: 'Sign in' }).click();
    console.log("Sign in clicado");

    await page.locator('[id="login_field"]').fill('Login-Teste');
    await page.locator('[id="password"]').fill('Senha-Teste');

    await page.click('[data-signin-label="Sign in"]');
    console.log("Clicado em login");

    await page.waitForTimeout(1000);  
    // Verifica se o alerta de erro de senha aparece
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

    await page.waitForTimeout(1000);  
});