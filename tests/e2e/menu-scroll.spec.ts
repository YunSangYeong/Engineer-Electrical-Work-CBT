import {test,expect} from '@playwright/test';
for(const [width,height] of [[390,480],[740,360]]) for(const input of ['wheel','touch']) {
 test(`메뉴 실제 ${input} 상하 이동 ${width}×${height}`,async({browser,baseURL})=>{
  const context=await browser.newContext({viewport:{width,height},hasTouch:true,isMobile:true});
  const page=await context.newPage();await page.goto(baseURL!);
  await page.addStyleTag({content:'html { font-size: 125%; }'});
  await page.getByRole('button',{name:'메뉴 열기'}).click();
  const menu=page.locator('.sidebar');await expect(menu).toHaveClass(/open/);await page.waitForTimeout(400);
  const cdp=await context.newCDPSession(page);
  async function scroll(down:boolean){
   if(input==='wheel'){await page.mouse.move(120,height/2);await page.mouse.wheel(0,down?1800:-1800);}
   else {
    const y1=down?height-50:80,y2=down?80:height-50;
    await cdp.send('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:[{x:120,y:y1}]});
    for(let i=1;i<=12;i++) {await cdp.send('Input.dispatchTouchEvent',{type:'touchMove',touchPoints:[{x:120,y:y1+(y2-y1)*i/12}]});await page.waitForTimeout(20);}
    await cdp.send('Input.dispatchTouchEvent',{type:'touchEnd',touchPoints:[]});
   }
   await page.waitForTimeout(350);
  }
  for(let i=0;i<4;i++) await scroll(true);
  expect(await menu.evaluate(el=>el.scrollTop)).toBeGreaterThan(0);
  const reset=page.getByRole('button',{name:'데이터 초기화',exact:true});
  await expect(reset).toBeInViewport();
  // Click in its current viewport position, without locator auto-scrolling.
  let box=await reset.boundingBox();await page.mouse.click(box!.x+box!.width/2,box!.y+box!.height/2);
  await expect(page.getByRole('dialog')).toBeVisible();await page.getByRole('button',{name:'돌아가기',exact:true}).click();
  for(let i=0;i<4;i++) await scroll(false);
  const dashboard=page.getByRole('navigation').getByRole('button',{name:'학습 대시보드',exact:true});await expect(dashboard).toBeInViewport();
  box=await dashboard.boundingBox();await page.mouse.click(box!.x+box!.width/2,box!.y+box!.height/2);
  await expect(menu).not.toHaveClass(/open/);
  await expect(page.getByRole('heading',{name:'전기공사기사 필기 CBT',exact:true})).toBeVisible();
  expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBe(true);
  await context.close();
 });
}
test('상시 안내 배너 없음, 손상 기록 경고 유지',async({page})=>{
 await page.goto('');await expect(page.locator('.criteria-note')).toHaveCount(0);
 await page.getByRole('button',{name:'모의시험 시작하기',exact:true}).click();await expect(page.locator('main .notice')).toHaveCount(0);
 await page.evaluate(()=>localStorage.setItem('Engineer-Electrical-Work-CBT:v1','{broken'));
 await page.reload();await expect(page.getByRole('alert')).toContainText('기존 데이터를 덮어쓰지 않고');
});
