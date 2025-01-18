import { test, expect } from "@playwright/test";
import { TIMEOUT } from "dns";
import { text } from "stream/consumers";

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

    await page.waitForTimeout(1000)

    //verificar elemento flutuante: starta --ui, botao direito e inspecionar o elemento flutuante -- Toast é a classe, e que tenha a escrita agradecemos...
    //primeiro faz clilcar no modal e depois verifica se realmente aparece
    await page.getByTestId('modal').getByText("Quero entrar na fila!").click()
    //Verifica se realmente aparece
    await expect(page.locator('.toast')).toHaveText('Agradecemos por compartilhar seus dados conosco. Em breve, nossa equipe entrará em contato!')
    await page.waitForTimeout(5000)
    await expect(page.locator('.toast')).toBeHidden({timeout: 5000})
}) 