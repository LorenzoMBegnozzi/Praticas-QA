import { test, expect } from "@playwright/test";

test("deve cadastras um lead na fila de espera", async ({ page }) => {
    await page.goto('http://localhost:3000');

    await page.getByRole('button', { name: /Aperte o play/ }).click() //clicar no botao q tem escrita nele

    await expect(
        page.getByTestId('modal').getByRole('heading')
    ).toHaveText('Fila de espera') // espero que o titulo do modelo modal tenha o texto fila de espera


    //await page.locator('#name').fill('lorenzobegnozzi@hotmail.com') //pelo id = name

    //await page.locator('input[name=name]').fill('lorenzobegnozzi@hotmail.com') //pelo name=name

    await page.getByPlaceholder('Seu nome completo').fill('Lorenzo Marzola') //pelo locator - descriçao oq deve ser inserido

    await page.getByPlaceholder('Seu email principal').fill("lorenzobegnozzi@hotmail.com")

    await page.getByText('Quero entrar na fila!').click() //clicar no botao q tem escrita nele 

    await page.waitForTimeout(1000)
}) 