import { test, expect } from "@playwright/test";
import { LadingPage } from "./pages/LandingPage";
import { measureMemory } from "vm";

test("deve cadastras um lead na fila de espera", async ({ page }) => {
    const landingPage = new LadingPage(page)

    await landingPage.visit()
    await landingPage.openLeadModal()
    await landingPage.submitLeadForm('Lorenzo Marzola','lorenzoteste@hotmail.com')

    const message = 'Agradecemos por compartilhar seus dados conosco. Em breve, nossa equipe entrará em contato!'

    await landingPage.toastHaveText(message)

})


test(" não deve cadastrar como email incorreto", async ({ page }) => {
    await page.goto('http://localhost:3000');

    await page.getByRole('button', { name: /Aperte o play/ }).click() //clicar no botao q tem escrita nele

    await expect(page.getByTestId('modal').getByRole('heading')).toHaveText('Fila de espera') // espero que o titulo do modelo modal tenha o texto fila de espera

    await page.getByPlaceholder('Informe seu nome').fill('Lorenzo Marzola') //pelo locator - descriçao oq deve ser inserido

    await page.getByPlaceholder('Informe seu email').fill("teste.com.br")

    await page.waitForTimeout(1000)

    await page.getByTestId('modal').getByText("Quero entrar na fila!").click()

    await expect(page.locator('.alert')).toHaveText('Email incorreto')
})


test(" não deve cadastrar quando o nome nao é preenchico", async ({ page }) => {
    await page.goto('http://localhost:3000');

    await page.getByRole('button', { name: /Aperte o play/ }).click() //clicar no botao q tem escrita nele

    await expect(page.getByTestId('modal').getByRole('heading')).toHaveText('Fila de espera') // espero que o titulo do modelo modal tenha o texto fila de espera

    await page.getByPlaceholder('Informe seu email').fill("teste@test.com")

    await page.waitForTimeout(1000)

    await page.getByTestId('modal').getByText("Quero entrar na fila!").click()

    await expect(page.locator('.alert')).toHaveText('Campo obrigatório')
})

test(" não deve cadastrar quando o e-mail nao é preenchico", async ({ page }) => {
    await page.goto('http://localhost:3000');

    await page.getByRole('button', { name: /Aperte o play/ }).click() //clicar no botao q tem escrita nele

    await expect(page.getByTestId('modal').getByRole('heading')).toHaveText('Fila de espera') // espero que o titulo do modelo modal tenha o texto fila de espera

    await page.getByPlaceholder('Informe seu nome').fill('Lorenzo Marzola')

    await page.waitForTimeout(1000)

    await page.getByTestId('modal').getByText("Quero entrar na fila!").click()

    await expect(page.locator('.alert')).toHaveText('Campo obrigatório')
})

test(" não deve cadastrar quando nenhum campo é preenchico", async ({ page }) => {
    await page.goto('http://localhost:3000');

    await page.getByRole('button', { name: /Aperte o play/ }).click() //clicar no botao q tem escrita nele

    await expect(page.getByTestId('modal').getByRole('heading')).toHaveText('Fila de espera') // espero que o titulo do modelo modal tenha o texto fila de espera

    await page.waitForTimeout(1000)

    await page.getByTestId('modal').getByText("Quero entrar na fila!").click()

    await expect(page.locator('.alert')).toHaveText([
        'Campo obrigatório',
        'Campo obrigatório'
    ]) //para quando tiver mais de um alerta com a mesma escrita

}) 