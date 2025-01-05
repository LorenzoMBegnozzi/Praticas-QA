import { test, expect } from '@playwright/test'

test.skip('Automaçao de checklist', async ({ page }) => {
    await page.goto("https://demo.playwright.dev/todomvc/#/")

    const newTodo = await page.getByPlaceholder('What needs to be done?')
    await newTodo.fill('Teste1');
    await newTodo.press('Enter');
    await newTodo.fill('Teste2 ');
    await newTodo.press('Enter')
    await page.waitForTimeout(3000);

    const fistTodo = page.getByTestId('todo-item').nth(0) //dizer que queremos o primeiro elemento 
    await fistTodo.getByRole('checkbox').check();
    await page.waitForTimeout(3000);

    const secondTodo = page.getByTestId('todo-item').nth(1) //dizer que queremos marcar o segundo elemento
    await secondTodo.getByRole('checkbox').check();
    await page.waitForTimeout(3000);

    await expect(secondTodo).not.toHaveClass('complete')
    await expect(fistTodo).not.toHaveClass('complete')
})

test('Handling Form', async ({ page }) => {
    await page.goto('https://demo.playwright.dev/todomvc/#/');
    const placeholder = '[placeholder = "What needs to be done?"]';
    await page.fill(placeholder, 'Teste1')
    await page.locator(placeholder).press('Enter')


    const checkbox = await page.locator('.toggle')
    await checkbox.check();
    await page.waitForTimeout(3000);
})