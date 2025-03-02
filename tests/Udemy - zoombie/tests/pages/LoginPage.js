const { expect } = require('@playwright/test')

export class LoginPage {

    constructor(page) {
        this.page = page
    }

    async visit(){
        await this.page.goto('http://localhost:3000/admin/login')

        const loginForm = this.page.locator('.login-form')
        await expect(loginForm).toBeVisible()

    }

    async login (email, password){
        await this.page.getByPlaceholder('E-mail').fill(email)
        await this.page.getByPlaceholder('Senha').fill(password)
        await this.page.getByText("Entrar").click()
    }

    async deslogar(){
        await this.page.waitForLoadState('networkidle') /*vai validar se esta na
        pagina de admin, depois q acabar todo o trafego de rede*/ 
        await expect(this.page).toHaveURL(/.*admin/)
    }
}
