const { expect } = require('@playwright/test')
export class LadingPage {

    constructor(page) {
        this.page = page
    }

    async visit() {
        await this.page.goto('http://localhost:3000');
    }

    async openLeadModal() {
        await this.page.getByRole('button', { name: /Aperte o play/ }).click() //clicar no botao q tem escrita nele

        await expect(this.page.getByTestId('modal').getByRole('heading')).toHaveText('Fila de espera') // espero que o titulo do modelo modal tenha o texto fila de espera
    }

    async submitLeadForm(name, email) {
        await this.page.getByPlaceholder('Informe seu nome').fill(name) //pelo locator - descriçao oq deve ser inserido
        await this.page.getByPlaceholder('Informe seu email').fill(email)

        await this.page.waitForTimeout(1000)

        await this.page.getByTestId('modal').getByText("Quero entrar na fila!").click()
    }

    async toastHaveText(message) {
        await expect(this.page.locator('.toast')).toHaveText(message)
        await expect(this.page.locator('.toast')).toBeHidden({ timeout: 5000 })
    }

    async alertHaveText(target){
       await expect(this.page.locator('.alert')).toHaveText(target)
    }
}