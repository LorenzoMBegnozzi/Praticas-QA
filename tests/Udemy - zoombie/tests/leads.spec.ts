import { test, expect } from "@playwright/test";
import { exec } from "child_process";
import { TIMEOUT } from "dns";
import { text } from "stream/consumers";

test("deve cadastras um lead na fila de espera", async ({ page }) => {
    await page.goto('http://localhost:3000');

    await page.getByRole('button', { name: /Aperte o play/ }).click() //clicar no botao q tem escrita nele

    await expect(
        page.getByTestId('modal').getByRole('heading')).toHaveText('Fila de espera') // espero que o titulo do modelo modal tenha o texto fila de espera

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


test(" não deve cadastrar como email incorreto", async ({ page }) => {
    await page.goto('http://localhost:3000');

    await page.getByRole('button', { name: /Aperte o play/ }).click() //clicar no botao q tem escrita nele

    await expect(
        page.getByTestId('modal').getByRole('heading')).toHaveText('Fila de espera') // espero que o titulo do modelo modal tenha o texto fila de espera

    await page.getByPlaceholder('Seu nome completo').fill('Lorenzo Marzola') //pelo locator - descriçao oq deve ser inserido

    await page.getByPlaceholder('Seu email principal').fill("teste.com.br")

    await page.waitForTimeout(1000)

    await page.getByTestId('modal').getByText("Quero entrar na fila!").click()

    await expect(page.locator('.alert')).toHaveText('Email incorreto')
}) 


test(" não deve cadastrar quando o nome nao é preenchico", async ({ page }) => {
    await page.goto('http://localhost:3000');

    await page.getByRole('button', { name: /Aperte o play/ }).click() //clicar no botao q tem escrita nele

    await expect(
        page.getByTestId('modal').getByRole('heading')).toHaveText('Fila de espera') // espero que o titulo do modelo modal tenha o texto fila de espera

    await page.getByPlaceholder('Seu email principal').fill("teste@test.com")

    await page.waitForTimeout(1000)

    await page.getByTestId('modal').getByText("Quero entrar na fila!").click()

    await expect(page.locator('.alert')).toHaveText('Campo obrigatório')
}) 

test(" não deve cadastrar quando o e-mail nao é preenchico", async ({ page }) => {
    await page.goto('http://localhost:3000');

    await page.getByRole('button', { name: /Aperte o play/ }).click() //clicar no botao q tem escrita nele

    await expect(page.getByTestId('modal').getByRole('heading')).toHaveText('Fila de espera') // espero que o titulo do modelo modal tenha o texto fila de espera

    await page.getByPlaceholder('Seu nome completo').fill('Lorenzo Marzola')

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