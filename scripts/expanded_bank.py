"""45 independently described exercise families, 20 conditions each.
No statutory thresholds, exam years, third-party questions, or official claims.
All quantities are idealized textbook conditions; not installation approval advice.
"""

def exercise(k, f, n):
    # returns kind, inputs, result, unit, topic, stem, formula/substitution, interpretation
    if k == 0:
        if f == 1:
            a,b=n+2,3
            return 'heatEnergy',[a,b],a*b,'kWh','전열·소비 전력량',f'일정한 유효전력 {a} kW인 전열기를 {b}시간 운전했다. 소비 전력량은?',f'W=Pt={a}×{b}', 'kW와 시간을 곱하면 kWh이다. 열효율을 곱한 유효 열량과 소비 전력량은 구별한다.'
        if f == 2:
            a,b=100*(n+10),20
            return 'luminousEfficacy',[a,b],a/b,'lm/W','조명·광원 광효율',f'소비전력이 {b} W인 광원이 광속 {a} lm을 방출한다. 광원 광효율은?',f'η=Φ/P={a}/{b}', '광원에서 방출한 광속을 전기 입력으로 나눈 값이며 작업면 조도와는 다르다.'
        if f == 3:
            a,b=1000,20+2*n
            return 'utilizedFlux',[a,b],a*b/100,'lm','조명·이용 광속',f'광원 총광속 {a} lm 중 작업면에 도달하는 비율이 {b}%이다. 작업면 입사 광속은?',f'Φ면=Φ원×u={a}×({b}/100)', '제시한 비율에 광속 손실이 포함되어 있으며 유지율 등 다른 계수를 추가하지 않는다.'
        if f == 4:
            a,b=n+5,4
            return 'jouleHeat',[a,b],a*a*b,'J','전열·발생 열량',f'저항 {b} Ω에 직류 {a} A를 정확히 1초 흘린다. 모두 열로 변환되는 에너지는?',f'Q=I²Rt={a}²×{b}×1', '초 단위를 사용한 전기 에너지 단위는 J이며 시간당 전력량 kWh와 다르다.'
        if f == 5:
            a,b=1000,500+10*n
            return 'heaterEfficiency',[a,b],100*b/a,'%','전열·열효율',f'전열 설비에 입력된 에너지가 {a} kJ이고 대상 물체가 얻은 유효 열량이 {b} kJ이다. 열효율은?',f'η=Q유효/W입력×100={b}/{a}×100', '두 에너지의 단위가 같아 그대로 나눌 수 있으며 열손실은 입력과 유효 열량의 차이다.'
        if f == 6:
            a,b,c=0.02,10*n,2
            return 'wireResistance',[a,b,c],a*b/c,'Ω','공사재료·도체 저항',f'비저항 {a} Ω·mm²/m, 길이 {b} m, 단면적 {c} mm²인 균일 도체 한 가닥의 저항은? (온도는 일정하다.)',f'R=ρl/A={a}×{b}/{c}', '비저항의 길이·면적 단위가 주어진 m와 mm²에 맞춰져 있으므로 별도 면적 단위 변환이 필요 없다.'
        if f == 7:
            a,b,c=10,20+n,0.00002
            return 'thermalExpansion',[a,b,c],a*b*c*1000,'mm','공사재료·열팽창',f'길이 {a} m인 도체의 선팽창계수는 {c} /K이다. 온도가 {b} K 상승할 때 늘어나는 길이는? (선형 팽창을 가정한다.)',f'Δl=αlΔT={c}×{a}×{b} m; mm로 환산하여 ×1000', '온도 차 1 K와 1 ℃의 크기는 같다. 구하는 값은 전체 길이가 아닌 증가분이다.'
        if f == 8:
            a,b=100*n,10
            return 'lightingDensity',[a,b],a/b,'W/m²','조명·설치 전력 밀도',f'바닥면적 {b} m²에 조명 유효전력 합계 {a} W가 설치되어 있다. 단위 면적당 조명 전력은?',f'p=P/A={a}/{b}', '이는 설치 전력의 면적당 값이며 법정 허용 한계나 조도를 판정하는 문제는 아니다.'
        if f == 9:
            a,b=n+2,5
            return 'batteryCapacity',[a,b],a*b,'Ah','전지·방전 전하량',f'이상적인 전지에서 일정 전류 {a} A로 {b}시간 방전했다. 이 시간 동안 방출한 전하량을 Ah로 나타내면?',f'C=It={a}×{b}', '온도·방전율에 따른 용량 변화와 손실을 무시한다. Ah는 전하량이며 에너지 Wh를 구하려면 전압이 추가로 필요하다.'
    if k == 1:
        if f == 1:
            a,b=n+2,2
            return 'feederDrop',[a,b],a*b,'V','배전·선로 전압 강하',f'직류 선로의 왕복 총저항이 {b} Ω이고 전류는 {a} A이다. 왕복 선로 전압 강하는?',f'ΔU=IR왕복={a}×{b}', '왕복 총저항이 이미 주어졌으므로 계수 2를 다시 곱하지 않는다.'
        if f == 2:
            a,b,c=100,n+2,0.8
            return 'phasePower',[a,b,c],3*a*b*c,'W','송배전·평형 3상 전력',f'평형 3상 부하의 상전압 {a} V, 상전류 {b} A, 역률 {c}이다. 3상 전체 유효전력은?',f'P=3V상I상cosφ=3×{a}×{b}×{c}', '상전압과 상전류가 주어져 계수 3을 사용한다. 선간전압으로 주어지는 식과 혼동하지 않는다.'
        if f == 3:
            a,b=1000,20*n
            return 'deliveryEfficiency',[a,b],a/(a+b)*100,'%','송배전·송전 효율',f'수전단 유효전력이 {a} kW, 선로 총손실이 {b} kW이다. 송전단 유효전력 대비 수전단 유효전력의 비율은? (소수 둘째 자리까지 반올림)',f'η=P수전/(P수전+P손실)×100={a}/({a}+{b})×100', '송전단 전력은 수전 전력과 손실의 합이다. 손실을 수전 전력에서 빼지 않는다.'
        if f == 4:
            a,b=10+n,50
            return 'powerFactor',[a,b],100*a/b,'%','전력 관리·역률',f'부하의 유효전력 {a} kW, 피상전력 {b} kVA이다. 역률을 백분율로 나타내면?',f'cosφ=P/S={a}/{b}; 백분율로 ×100', '유효전력은 피상전력보다 작게 주어졌으며 역률만으로 진상·지상을 구별하지 않는다.'
        if f == 5:
            a,b=100,20+n
            return 'demandFactor',[a,b],100*b/a,'%','전력 관리·수용률',f'설비용량 합계가 {a} kW이고 측정한 최대수요전력이 {b} kW이다. 수용률은?',f'd=P최대/P설비×100={b}/{a}×100', '수용률은 최대수요전력을 설비용량으로 나눈 값이며 평균부하를 쓰는 부하율과 다르다.'
        if f == 6:
            a,b=100,50+n
            return 'diversityFactor',[a,b],a/b,'배','전력 관리·부등률',f'개별 부하 최대수요전력의 합이 {a} kW, 합성 부하 최대수요전력이 {b} kW이다. 부등률은? (소수 둘째 자리까지 반올림)',f'D=ΣP개별최대/P합성최대={a}/{b}', '분자는 개별 최대값의 합이고 분모는 같은 시각들의 합성 최대값이다. 부등률은 여기서 1 이상이다.'
        if f == 7:
            a,b=100,20+n
            return 'loadFactor',[a,b],100*b/a,'%','전력 관리·부하율',f'같은 기간 최대부하 {a} kW, 평균부하 {b} kW인 설비의 부하율은?',f'LF=P평균/P최대×100={b}/{a}×100', '비교하는 평균과 최대는 동일 기간이다. 설비용량을 분모로 사용하는 수용률과 다르다.'
        if f == 8:
            a,b=100+5*n,40
            return 'reactiveCompensation',[a,b],a-b,'kvar','전력 관리·무효전력 보상',f'부하의 지상 무효전력은 {a} kvar이다. 병렬 콘덴서가 {b} kvar를 공급할 때 계통이 공급할 지상 무효전력은? (고조파·손실 무시)',f'Q계통=Q부하-Q콘덴서={a}-{b}', '이 조건에서는 콘덴서의 무효전력이 부하보다 작으므로 보상 후에도 지상이다.'
        if f == 9:
            a,b=200+10*n,200
            return 'perUnitVoltage',[a,b],a/b,'pu','송배전·단위법',f'기준 전압이 {b} kV인 계통에서 실제 전압이 {a} kV이다. 전압의 pu 값은?',f'Vpu=V실제/V기준={a}/{b}', '같은 종류의 전압과 같은 단위를 비교한다. pu 값은 무차원이며 %로 나타낼 때에만 100을 곱한다.'
    if k == 2:
        if f == 1:
            a,b,c=1000,100,20+n
            return 'turnsVoltage',[a,b,c],c*b/a,'V','변압기·권수비',f'이상 변압기의 1차 권수 {a}회, 2차 권수 {b}회, 1차 실효전압 {c} V이다. 무부하 2차 실효전압은?',f'V₂=V₁N₂/N₁={c}×{b}/{a}', '여자 전류와 누설 임피던스를 무시하며 전압비는 권수비와 같다.'
        if f == 2:
            a,b=4*n,0.5
            return 'copperLoad',[a,b],a*b*b,'W','변압기·부하율과 동손',f'정격 전류에서 동손이 {a} W인 변압기를 정격 전류의 {b}배로 운전한다. 저항이 일정할 때 동손은?',f'Pcu=x²Pcu정격={b}²×{a}', '동손은 전류의 제곱에 비례한다. 철손을 포함한 총손실을 묻는 문제가 아니다.'
        if f == 3:
            a,b=1000,10*n
            return 'machineEfficiency',[a,b],100*a/(a+b),'%','회전기·효율',f'전동기의 기계 출력이 {a} W, 전체 손실이 {b} W이다. 효율은? (소수 둘째 자리까지 반올림)',f'η=P출력/(P출력+P손실)×100={a}/({a}+{b})×100', '전기 입력은 기계 출력과 손실을 합한 값이다. 손실률을 출력 기준으로 바로 빼지 않는다.'
        if f == 4:
            a,b=100*n,10
            return 'shaftTorque',[a,b],a/b,'N·m','회전기·축 토크',f'각속도 {b} rad/s로 회전하는 축의 기계 출력은 {a} W이다. 축 토크는?',f'T=P/ω={a}/{b}', '회전속도가 각속도로 주어졌으므로 rpm을 rad/s로 바꾸는 계수를 추가하지 않는다.'
        if f == 5:
            a,b=n+2,5
            return 'dcEmf',[a,b],a*b,'V','직류기·유기 기전력',f'직류 발전기의 주어진 운전 범위에서 E=kω이고 k={b} V·s/rad로 일정하다. 각속도 {a} rad/s에서 기전력은?',f'E=kω={b}×{a}', '자속이 일정하며 제시한 계수에 기계 구조와 자속이 반영되어 있다.'
        if f == 6:
            a,b,c=200,n+2,2
            return 'generatorTerminal',[a,b,c],a-b*c,'V','직류 발전기·단자전압',f'직류 발전기 유기 기전력 {a} V, 전기자 전류 {b} A, 전기자 저항 {c} Ω이다. 브러시 전압 강하를 무시한 단자전압은?',f'V=E-IaRa={a}-{b}×{c}', '발전기에서는 내부 저항 강하를 기전력에서 뺀다. 전동기 입력 단자전압의 식과 구별한다.'
        if f == 7:
            a,b=40+n,4
            return 'synchronousSpeed',[a,b],120*a/b,'min⁻¹','교류기·동기속도',f'주파수 {a} Hz, 극수 {b}극인 교류기의 동기속도는?',f'Ns=120f/p=120×{a}/{b}', '극수는 극쌍 수가 아니라 전체 극수이며 답의 단위는 분당 회전수이다.'
        if f == 8:
            a,b=50,n
            return 'rotorFrequency',[a,b],a*b/100,'Hz','유도전동기·회전자 주파수',f'유도전동기의 전원 주파수는 {a} Hz, 슬립은 {b}%이다. 회전자 전류 주파수는?',f'f₂=sf₁=({b}/100)×{a}', '슬립을 비율로 변환해야 한다. 기계 회전 주파수와 회전자 전류의 전기적 주파수는 다르다.'
        if f == 9:
            a,b=100*n,100
            return 'dcInputCurrent',[a,b],a/b,'A','직류 전동기·입력 전류',f'직류 전동기의 전기 입력이 {a} W이고 단자전압이 {b} V이다. 단자 입력 전류는?',f'I=P입력/V={a}/{b}', '주어진 전력은 기계 출력이 아니라 전기 입력이므로 효율을 추가로 적용하지 않는다.'
    if k == 3:
        if f == 1:
            a,b=10*n,5
            return 'ohmCurrent',[a,b],a/b,'A','직류·옴의 법칙',f'저항 {b} Ω에 직류 전압 {a} V를 가한다. 정상상태 전류는?',f'I=V/R={a}/{b}', '이상적인 순저항이며 전압원 내부 저항은 무시한다.'
        if f == 2:
            a,b=2*n,2*n
            return 'parallelResistance',[a,b],a*b/(a+b),'Ω','회로·병렬 합성저항',f'{a} Ω과 {b} Ω인 두 저항을 병렬 연결했다. 합성저항은?',f'R=R₁R₂/(R₁+R₂)={a}×{b}/({a}+{b})', '병렬 합성저항은 각 저항보다 작다. 직렬처럼 저항값을 더하지 않는다.'
        if f == 3:
            a,b=2*n,10
            return 'capacitorCharge',[a,b],a*b,'μC','정전용량·전하',f'정전용량 {a} μF인 이상 콘덴서에 전압 {b} V를 가했다. 저장 전하량은?',f'Q=CV={a} μF×{b} V', 'μF와 V를 곱하면 μC가 된다. 에너지와 전하량을 구별한다.'
        if f == 4:
            a,b=2,n+2
            return 'inductorVoltage',[a,b],a*b,'V','인덕턴스·유도 전압',f'인덕턴스 {a} H인 이상 코일에서 전류가 일정하게 초당 {b} A 증가한다. 수동 부호 규약에서 코일 양단 전압의 크기는?',f'|v|=L|di/dt|={a}×{b}', '저항 손실을 무시하며 전류 변화율에 인덕턴스를 곱한다.'
        if f == 5:
            a,b=10*n,10
            return 'rcTime',[a,b],a*b,'ms','과도현상·RC 시정수',f'저항 {a} kΩ과 정전용량 {b} μF인 직렬 RC 회로의 시정수는?',f'τ=RC={a}×10³×{b}×10⁻⁶ s; ms로 환산하여 ×1000', '시정수는 완전 충전 시간이 아니다. kΩ와 μF의 곱의 단위는 ms이다.'
        if f == 6:
            a,b=2,n+2
            return 'rlTime',[a,b],1000*a/b,'ms','과도현상·RL 시정수',f'인덕턴스 {a} H, 직렬 저항 {b} Ω인 RL 회로의 시정수는? (소수 둘째 자리까지 반올림)',f'τ=L/R={a}/{b} s; ms로 환산하여 ×1000', '직렬 RL 회로의 자연응답에서 전류는 이 시정수로 변한다. RC 시정수 식과 구별한다.'
        if f == 7:
            a,b=2*n,5
            return 'amplifierGain',[a,b],a*b,'V','제어공학·정적 이득',f'선형 블록의 입력이 {a} V이고 무차원 정적 이득은 {b}이다. 포화가 없는 정상상태 출력은?',f'y=Ku={b}×{a}', '선형·비포화라는 조건에서만 주어진 이득을 그대로 적용한다.'
        if f == 8:
            a,b=2*n,1
            return 'feedbackGain',[a,b],a/(1+a*b),'배','제어공학·음의 피드백',f'전달함수의 정상상태 값이 G={a}, H={b}인 음의 피드백 계통이다. 폐루프 정상상태 이득은? (소수 둘째 자리까지 반올림)',f'T=G/(1+GH)={a}/(1+{a}×{b})', '음의 피드백이므로 분모는 1+GH이다. 양의 피드백의 부호와 혼동하지 않는다.'
        if f == 9:
            a,b,c=100,n+2,0.5
            return 'acRealPower',[a,b,c],a*b*c,'W','교류·단상 유효전력',f'단상 정현파 부하의 실효전압 {a} V, 실효전류 {b} A, 역률 {c}이다. 유효전력은?',f'P=VIcosφ={a}×{b}×{c}', '실효값이므로 최댓값을 실효값으로 바꾸는 √2 계수를 추가하지 않는다.'
    if k == 4:
        suffix=' (주어진 이상화 측정 조건의 계산이며 법정 시험값·허용값·적합 판정을 묻지 않는다.)'
        if f == 1:
            a,b=500,5*n
            return 'insulationResistance',[a,b],a/b,'MΩ','안전 측정 기초·절연저항',f'시험 전압 {a} V에서 저항성 누설 전류가 {b} μA로 측정된다. 옴의 법칙으로 추정한 저항은? (소수 둘째 자리까지 반올림)'+suffix,f'R=U/I={a}/({b}×10⁻⁶) Ω; MΩ로 환산하여 ÷10⁶', '저항성 정상 누설만 가정한다. 실제 적합 판정에는 적용 규정·시험 조건의 별도 확인이 필요하다.'
        if f == 2:
            a,b=100+5*n,100
            return 'potentialDifference',[a,b],a-b,'V','안전 측정 기초·전위차',f'동일 기준점에 대해 두 도전부의 전위가 각각 {a} V와 {b} V이다. 두 도전부 사이 전위차의 크기는?'+suffix,f'|ΔV|=|V₁-V₂|=|{a}-{b}|', '전위의 합이 아니라 차를 구한다. 전위차 계산만으로 접촉 안전성을 판정하지 않는다.'
        if f == 3:
            a,b=2*n,2
            return 'earthTestResistance',[a,b],a/b,'Ω','안전 측정 기초·접지저항 환산',f'이상적인 분리 측정에서 대상 접지극 전압 상승 {a} V와 주입 전류 {b} A를 얻었다. 다른 경로·계기 오차를 무시한 저항은?'+suffix,f'R=U/I={a}/{b}', '실제 접지 측정은 보조극 배치·병렬 경로·잡음의 영향을 받는다. 이 문항은 이상적인 전압·전류 환산만 다룬다.'
        if f == 4:
            a,b=10*n,1000
            return 'touchCurrent',[a,b],1000*a/b,'mA','안전 계산 기초·저항 모델 전류',f'가상 인체를 일정 저항 {b} Ω으로만 모델링하고 양단에 {a} V를 가정한다. 이 모델의 전류는?'+suffix,f'I=U/R={a}/{b} A; mA로 환산하여 ×1000', '인체 임피던스는 실제로 조건에 따라 달라진다. 일정 저항 모델의 계산을 인체 안전 보장으로 해석하면 안 된다.'
        if f == 5:
            a,b=200,2*n
            return 'faultLoopCurrent',[a,b],a/b,'A','안전 계산 기초·고장 루프',f'이상 전원의 전압이 {a} V, 고장 루프의 전체 저항성 임피던스가 {b} Ω이다. 고장 전류의 추정값은? (소수 둘째 자리까지 반올림)'+suffix,f'If=U/Zs={a}/{b}', '보호장치의 차단 시간·동작 전류 검증은 별개다. 이 전류 계산만으로 자동 차단 적합성을 판단하지 않는다.'
        if f == 6:
            a,b=100*n,100
            return 'storedCapacitorEnergy',[a,b],0.5*a*1e-6*b*b,'J','안전 계산 기초·잔류 저장 에너지',f'정전용량 {a} μF의 콘덴서가 {b} V로 충전되어 있다. 이상적인 저장 에너지는?'+suffix,f'W=CV²/2=({a}×10⁻⁶)×{b}²/2', '전원 분리만으로 저장 에너지가 즉시 사라지지 않는다. 실제 작업에서는 별도의 안전 절차가 필요하다.'
        if f == 7:
            a,b=2*n,2
            return 'currentDensity',[a,b],a/b,'A/mm²','안전 계산 기초·전류 밀도',f'단면적 {b} mm²에 균일하게 분포한 전류가 {a} A이다. 평균 전류 밀도는?'+suffix,f'J=I/A={a}/{b}', '전류 밀도만으로 허용전류를 결정하지 않는다. 포설·주위온도·절연 종류 등은 별도로 확인해야 한다.'
        if f == 8:
            a,b=100+5*n,100
            return 'testLeadCorrection',[a,b],a-b,'mΩ','안전 측정 기초·리드선 보정',f'2선식 측정 총저항이 {a} mΩ, 같은 조건에서 측정한 리드선 두 가닥의 총저항이 {b} mΩ이다. 단순 직렬 모델로 보정한 대상 저항은?'+suffix,f'R대상=R측정-R리드={a}-{b}', '동일한 접촉 조건을 가정한다. 작은 저항의 정밀 측정에서는 접촉저항·계기 오차를 별도로 고려한다.'
        if f == 9:
            a,b=2*n,2*n
            return 'parallelInsulation',[a,b],a*b/(a+b),'MΩ','안전 측정 기초·병렬 누설 경로',f'두 독립 저항성 누설 경로의 절연저항이 각각 {a} MΩ과 {b} MΩ이다. 병렬 합성 저항은?'+suffix,f'R합=R₁R₂/(R₁+R₂)={a}×{b}/({a}+{b})', '병렬 누설 경로가 추가되면 전체 저항은 감소한다. 각 회로의 검사 필요성과 법규 적합 판정은 별개다.'
    raise ValueError((k,f,n))


def additional_questions(subjects):
    from decimal import Decimal, ROUND_HALF_UP
    def rounded(v):
        return Decimal(str(v)).quantize(Decimal('0.01'),rounding=ROUND_HALF_UP)
    def fmt(v):
        return format(rounded(v),'f').rstrip('0').rstrip('.') if '.' in format(rounded(v),'f') else str(v)
    rows=[]
    for k,subject in enumerate(subjects):
        for f in range(1,10):
            for n in range(1,21):
                kind,values,result,unit,topic,stem,formula,meaning=exercise(k,f,n)
                answer=fmt(result)
                choices=[f'{fmt(rounded(result)+i)} {unit}' for i in (0,1,2,3)]
                rotation=(n+f)%4
                choices=choices[rotation:]+choices[:rotation]
                rows.append(dict(id=f'EWC-{k+1}-F{f+1:02}-{n:03}',subject=subject,topic=topic,question=stem,choices=choices,answer=choices.index(f'{answer} {unit}')+1,explanation=f'조건에서 {formula} = {answer} {unit}. {meaning}',difficulty='중' if f in (6,8) else '하',year=None,session=None,type='original',sourceUrl='https://github.com/YunSangYeong/Engineer-Electrical-Work-CBT',verificationStatus='reviewed',reviewNote='AI 일반 전기 지식 기반 자체 제작 계산 조건 변형. 템플릿의 조건·수식·단위·해설 내부 검토 및 별도 TypeScript 수치·보기 검증 수행. 공식 출제기준 대조·외부 전문가 검수 미실시. 저장소는 작성 위치이며 외부 정답 증빙이 아님.',version='main',rights='자체 제작 · CC BY 4.0 · Engineer-Electrical-Work-CBT contributors 표시',family=f'EWC-F{k+1}-{f+1:02}',calculation=dict(kind=kind,values=values,result=float(rounded(result)),unit=unit,precision=2)))
    return rows
