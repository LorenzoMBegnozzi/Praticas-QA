import {test, expect} from "@playwright/test"


test.skip('interaoes avancadas', async ({page}) => {
    await page.goto('http://127.0.0.1:5500/tests/Workshop_3/index.html')
    await page.hover('button#hover-me')
    expect(await page.textContent('button#hover-me')).toContain('Text Changed!'); //espera que o botao hover-me altere para text changed

    await page.click('button#context-menu', {button: "right"});
    expect(await page.getByText('Context Menu Appears!').textContent()).toContain('Context Menu Appears!');

    await page.dblclick('button#double-click')
    expect (await page.locator('img').count()).toBe(1); 
})

test.skip('Pegar e soltar', async({page}) => {
    await page.goto('http://127.0.0.1:5500/tests/Workshop_3/index.html')
    //await page.dragAndDrop('.drag-source','.drop-target');
    //expect (await page.textContent('.drop-target')).toContain('Success')
    //await page.waitForTimeout(3000)
    await page.locator('.drag-source').hover();
    await page.mouse.down();
    await page.locator('.drop-target').hover();
    expect(await page.textContent('.drop-target')).toContain("Success")
})

test('manipulação de iframe', async ({page}) => {
    await page.goto('http://127.0.0.1:5500/tests/Workshop_3/index.html')
    const inputSelector = '#iframa-input'
    
})
