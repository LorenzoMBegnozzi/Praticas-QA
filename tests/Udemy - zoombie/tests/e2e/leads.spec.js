const { test, expect } = require('@playwright/test')
const {LadingPage} = require('../pages/LandingPage')

let landingPage  

test("deve cadastras um lead na fila de espera", async ({ page }) => {
    const landingPage = new LadingPage(page)

    await landingPage.visit()
    await landingPage.openLeadModal()
    await landingPage.submitLeadForm('Lorenzo Marzola', 'lorenzoteste@hotmail.com')

    const message = 'Agradecemos por compartilhar seus dados conosco. Em breve, nossa equipe entrará em contato!'

    await landingPage.toastHaveText(message)

})

test(" não deve cadastrar como email incorreto", async ({ page }) => {
    const landingPage = new LadingPage(page)

    await landingPage.visit()
    await landingPage.openLeadModal()
    await landingPage.submitLeadForm('Lorenzo Marzola', 'emailerrado.com')

    await landingPage.alertHaveText('Email incorreto')
})

test(" não deve cadastrar quando o nome nao é preenchico", async ({ page }) => {
    const landingPage = new LadingPage(page)

    await landingPage.visit()
    await landingPage.openLeadModal()
    await landingPage.submitLeadForm('','emailteste@hotmail.com')

    await landingPage.alertHaveText('Campo obrigatório')
})

test(" não deve cadastrar quando o e-mail nao é preenchico", async ({ page }) => {
    const landingPage = new LadingPage(page)

    await landingPage.visit()
    await landingPage.openLeadModal()
    await landingPage.submitLeadForm('Lorenzo Marzola', '')


    await landingPage.alertHaveText('Campo obrigatório')
})

test(" não deve cadastrar quando nenhum campo é preenchico", async ({ page }) => {
    const landingPage = new LadingPage(page)

    await landingPage.visit()
    await landingPage.openLeadModal()
    await landingPage.submitLeadForm('', '')


    await landingPage.alertHaveText([
        'Campo obrigatório',
        'Campo obrigatório'
    ]) //para quando tiver mais de um alerta com a mesma escrita

}) 