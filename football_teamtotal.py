from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time
# Create a ChromeOptions instance
options = webdriver.ChromeOptions()

# Replace this with the actual path to your Chrome user profile directory
# options.add_argument("user-data-dir=C:\\Users\\JS guru\\AppData\\Local\\Google\\Chrome\\User Data")

# Disable the "DevToolsActivePort" check, as it can sometimes cause issues
options.add_argument("--disable-dev-shm-usage")

# Disable the "sandbox" mode if you encounter issues
options.add_argument("--no-sandbox")

# Create a Chrome webdriver instance with the options
driver = webdriver.Chrome(options=options)

driver.maximize_window()
# Open a website
driver.get("https://playerstats.football/premier-league/liverpool")

driver.find_element(By.XPATH, '/html/body/div[2]/nav/div/div[3]/a[1]').click()
# Find the one page table element
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('oscarthagando@hotmail.com')
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('HiScott!')
driver.find_element(By.XPATH, '/html/body/div/div/div[2]/form/div[4]/button').click()
try:
    driver.find_element(By.XPATH, '//*[@id="content-wrapper"]/div[1]/div[2]/div/div[1]/div[1]/div/div[2]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="content-wrapper"]/div[1]/div[2]/div/div[1]/div[1]/div/div[3]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="content-wrapper"]/div[1]/div[2]/div/div[1]/div[1]/div/div[4]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="content-wrapper"]/div[1]/div[2]/div/div[1]/div[1]/div/div[5]').click()
    time.sleep(1)
except:
    pass
element = driver.find_element(By.XPATH, '//*[@id="statsFilter"]')
actions = ActionChains(driver)
actions.click(element)  # Perform a click action on the element
for _ in range(3):
    actions.key_down(Keys.DOWN)  # Press down the "down" key
    actions.key_up(Keys.DOWN)  # Press down the Control key (modify the key if needed)
actions.key_down(Keys.ENTER)
actions.key_up(Keys.ENTER)
actions.perform()  # Perform the action
time.sleep(1)
l = 0
while l<4:
    if l == 0:
        season = '20_21'
    if l == 1:
        season = '21_22'
    if l == 2:
        season = '22_23'
    if l == 3:
        season = '23_24'
    Player_list = []
    A_list = []
    B_list = []
    C_list = []    
    D_list = []    
    E_list = []    
    F_list = []    
    G_list = []    
    H_list = []    
    I_list = []    
    J_list = []    
    K_list = []    
    L_list = []    
    M_list = []    
    N_list = []    
    O_list = []    
    P_list = []    
    Q_list = []    
    R_list = []    
    S_list = []    
    T_list = []    
    U_list = []    
    V_list = []    
    W_list = []    
    X_list = []    
    Y_list = []    
    Z_list = []    
    A1_list = []    
    B1_list = []    
    C1_list = []    
    D1_list = []    
    E1_list = []    
    F1_list = []    
    G1_list = []    
    H1_list = []    
    J1_list = []    
    K1_list = []    
    L1_list = []    
    M1_list = []    
    N1_list = []    

    Rows = driver.find_elements(By.XPATH, '//*[@id="totalsTable"]/div/div')

    for i in range(2, len(Rows)):
        try:
            Player = Rows[i].find_element(By.CLASS_NAME, 'stat__player').text
        except:
            Player = "none"
        print('Player:', Player)
        Player_list.append(Player)
        columnss = Rows[i].find_elements(By.CLASS_NAME, 'stat__fixture')
        columns = []
        for element in columnss:
            if 'hidden' not in element.get_attribute('class'):
                columns.append(element)        
        print(len(columnss))
        print(len(columns))
        if i == 2:
            try:
                A = columns[0].text
                B = columns[1].find_element(By.TAG_NAME, 'img').get_attribute('title')
                C = columns[2].find_element(By.TAG_NAME, 'img').get_attribute('title')
                D = columns[3].find_element(By.TAG_NAME, 'img').get_attribute('title')
                E = columns[4].find_element(By.TAG_NAME, 'img').get_attribute('title')
                F = columns[5].find_element(By.TAG_NAME, 'img').get_attribute('title')
                G = columns[6].find_element(By.TAG_NAME, 'img').get_attribute('title')
                H = columns[7].find_element(By.TAG_NAME, 'img').get_attribute('title')
                I = columns[8].find_element(By.TAG_NAME, 'img').get_attribute('title')
                J = columns[9].find_element(By.TAG_NAME, 'img').get_attribute('title')
                K = columns[10].find_element(By.TAG_NAME, 'img').get_attribute('title')
                L = columns[11].find_element(By.TAG_NAME, 'img').get_attribute('title')
                M = columns[12].find_element(By.TAG_NAME, 'img').get_attribute('title')
                N = columns[13].find_element(By.TAG_NAME, 'img').get_attribute('title')
                O = columns[14].find_element(By.TAG_NAME, 'img').get_attribute('title')
                P = columns[15].find_element(By.TAG_NAME, 'img').get_attribute('title')
                Q = columns[16].find_element(By.TAG_NAME, 'img').get_attribute('title')
                R = columns[17].find_element(By.TAG_NAME, 'img').get_attribute('title')
                S = columns[18].find_element(By.TAG_NAME, 'img').get_attribute('title')
                T = columns[19].find_element(By.TAG_NAME, 'img').get_attribute('title')
                U = columns[20].find_element(By.TAG_NAME, 'img').get_attribute('title')
                V = columns[21].find_element(By.TAG_NAME, 'img').get_attribute('title')
                W = columns[22].find_element(By.TAG_NAME, 'img').get_attribute('title')
                X = columns[23].find_element(By.TAG_NAME, 'img').get_attribute('title')
                Y = columns[24].find_element(By.TAG_NAME, 'img').get_attribute('title')
                Z = columns[25].find_element(By.TAG_NAME, 'img').get_attribute('title')
                A1 = columns[26].find_element(By.TAG_NAME, 'img').get_attribute('title')
                B1 = columns[27].find_element(By.TAG_NAME, 'img').get_attribute('title')
                C1 = columns[28].find_element(By.TAG_NAME, 'img').get_attribute('title')
                D1 = columns[29].find_element(By.TAG_NAME, 'img').get_attribute('title')
                E1 = columns[30].find_element(By.TAG_NAME, 'img').get_attribute('title')
                
                F1 = columns[31].find_element(By.TAG_NAME, 'img').get_attribute('title')
                G1 = columns[32].find_element(By.TAG_NAME, 'img').get_attribute('title')
                H1 = columns[33].find_element(By.TAG_NAME, 'img').get_attribute('title')
                J1 = columns[34].find_element(By.TAG_NAME, 'img').get_attribute('title')
                K1 = columns[35].find_element(By.TAG_NAME, 'img').get_attribute('title')
                L1 = columns[36].find_element(By.TAG_NAME, 'img').get_attribute('title')
                M1 = columns[37].find_element(By.TAG_NAME, 'img').get_attribute('title')
                N1 = columns[38].find_element(By.TAG_NAME, 'img').get_attribute('title')
            except:
                A = ""  
                B = ""  
                C = ""  
                D = ""  
                E = ""  
                F = ""  
                G = ""  
                H = ""  
                I = ""  
                J = ""  
                K = ""  
                L = ""  
                M = ""  
                N = ""  
                O = ""  
                P = ""  
                Q = ""  
                R = ""  
                S = ""  
                T = ""  
                U = ""  
                V = ""  
                W = ""  
                X = ""  
                Y = ""  
                Z = ""  
                A1 = ""  
                B1 = ""  
                C1 = ""  
                D1 = ""  
                E1 = ""  
                
                F1 = ""  
                G1 = ""  
                H1 = ""  
                J1 = ""  
                K1 = ""  
                L1 = ""  
                M1 = ""  
                N1 = ""  
            A_list.append(A)
            B_list.append(B)
            C_list.append(C)
            D_list.append(D)
            E_list.append(E)
            F_list.append(F)
            G_list.append(G)
            H_list.append(H)
            I_list.append(I)
            J_list.append(J)
            K_list.append(K)
            L_list.append(L)
            M_list.append(M)
            N_list.append(N)
            O_list.append(O)
            P_list.append(P)
            Q_list.append(Q)
            R_list.append(R)
            S_list.append(S)
            T_list.append(T)
            U_list.append(U)
            V_list.append(V)
            W_list.append(W)
            X_list.append(X)
            Y_list.append(Y)
            Z_list.append(Z)
            A1_list.append(A1)
            B1_list.append(B1)
            C1_list.append(C1)
            D1_list.append(D1)
            E1_list.append(E1)
            
            F1_list.append(F1)
            G1_list.append(G1)
            H1_list.append(H1)
            J1_list.append(J1)
            K1_list.append(K1)
            L1_list.append(L1)
            M1_list.append(M1)
            N1_list.append(N1)
        if i == 3 or i == 4:
            try:
                A = columns[0].text
                B = columns[1].text
                C = columns[2].text
                D = columns[3].text
                E = columns[4].text
                F = columns[5].text
                G = columns[6].text
                H = columns[7].text
                I = columns[8].text
                J = columns[9].text
                K = columns[10].text
                L = columns[11].text
                M = columns[12].text
                N = columns[13].text
                O = columns[14].text
                P = columns[15].text
                Q = columns[16].text
                R = columns[17].text
                S = columns[18].text
                T = columns[19].text
                U = columns[20].text
                V = columns[21].text
                W = columns[22].text
                X = columns[23].text
                Y = columns[24].text
                Z = columns[25].text
                A1 = columns[26].text
                B1 = columns[27].text
                C1 = columns[28].text
                D1 = columns[29].text
                E1 = columns[30].text
                
                F1 = columns[31].text
                G1 = columns[32].text
                H1 = columns[33].text
                J1 = columns[34].text
                K1 = columns[35].text
                L1 = columns[36].text
                M1 = columns[37].text
                N1 = columns[38].text
            except:
                A = ""  
                B = ""  
                C = ""  
                D = ""  
                E = ""  
                F = ""  
                G = ""  
                H = ""  
                I = ""  
                J = ""  
                K = ""  
                L = ""  
                M = ""  
                N = ""  
                O = ""  
                P = ""  
                Q = ""  
                R = ""  
                S = ""  
                T = ""  
                U = ""  
                V = ""  
                W = ""  
                X = ""  
                Y = "" 
                Z = ""  
                A1 = ""  
                B1 = ""  
                C1 = ""  
                D1 = ""  
                E1 = ""  
                
                F1 = ""  
                G1 = ""  
                H1 = ""  
                J1 = ""  
                K1 = ""  
                L1 = ""  
                M1 = ""  
                N1 = "" 
            A_list.append(A)
            B_list.append(B)
            C_list.append(C)
            D_list.append(D)
            E_list.append(E)
            F_list.append(F)
            G_list.append(G)
            H_list.append(H)
            I_list.append(I)
            J_list.append(J)
            K_list.append(K)
            L_list.append(L)
            M_list.append(M)
            N_list.append(N)
            O_list.append(O)
            P_list.append(P)
            Q_list.append(Q)
            R_list.append(R)
            S_list.append(S)
            T_list.append(T)
            U_list.append(U)
            V_list.append(V)
            W_list.append(W)
            X_list.append(X)
            Y_list.append(Y)
            Z_list.append(Z)
            A1_list.append(A1)
            B1_list.append(B1)
            C1_list.append(C1)
            D1_list.append(D1)
            E1_list.append(E1)
            
            F1_list.append(F1)
            G1_list.append(G1)
            H1_list.append(H1)
            J1_list.append(J1)
            K1_list.append(K1)
            L1_list.append(L1)
            M1_list.append(M1)
            N1_list.append(N1)
        else:
            try:
                Upper_A = columns[0].find_element(By.TAG_NAME, 'div').text
                Lower_A = columns[0].find_element(By.TAG_NAME, 'span').text
                A = Upper_A + "_" + Lower_A
                if A == "_":
                    A = ""
                Upper_B = columns[1].find_element(By.TAG_NAME, 'div').text
                Lower_B = columns[1].find_element(By.TAG_NAME, 'span').text
                B = Upper_B + "_" + Lower_B
                if B == "_":
                    B = ""
                Upper_C = columns[2].find_element(By.TAG_NAME, 'div').text
                Lower_C = columns[2].find_element(By.TAG_NAME, 'span').text
                C = Upper_C + "_" + Lower_C
                if C == "_":
                    C = ""
                Upper_D = columns[3].find_element(By.TAG_NAME, 'div').text
                Lower_D = columns[3].find_element(By.TAG_NAME, 'span').text
                D = Upper_D + "_" + Lower_D
                if D == "_":
                    D = ""
                Upper_E = columns[4].find_element(By.TAG_NAME, 'div').text
                Lower_E = columns[4].find_element(By.TAG_NAME, 'span').text
                E = Upper_E + "_" + Lower_E
                if E == "_":
                    E = ""
                Upper_F = columns[5].find_element(By.TAG_NAME, 'div').text
                Lower_F = columns[5].find_element(By.TAG_NAME, 'span').text
                F = Upper_F + "_" + Lower_F
                if F == "_":
                    F = ""
                Upper_G = columns[6].find_element(By.TAG_NAME, 'div').text
                Lower_G = columns[6].find_element(By.TAG_NAME, 'span').text
                G = Upper_G + "_" + Lower_G
                if G == "_":
                    G = ""
                Upper_H = columns[7].find_element(By.TAG_NAME, 'div').text
                Lower_H = columns[7].find_element(By.TAG_NAME, 'span').text
                H = Upper_H + "_" + Lower_H
                if H == "_":
                    H = ""
                Upper_I = columns[8].find_element(By.TAG_NAME, 'div').text
                Lower_I = columns[8].find_element(By.TAG_NAME, 'span').text
                I = Upper_I + "_" + Lower_I
                if I == "_":
                    I = ""
                Upper_J = columns[9].find_element(By.TAG_NAME, 'div').text
                Lower_J = columns[9].find_element(By.TAG_NAME, 'span').text
                J = Upper_J + "_" + Lower_J
                if J == "_":
                    J = ""
                Upper_K = columns[10].find_element(By.TAG_NAME, 'div').text
                Lower_K = columns[10].find_element(By.TAG_NAME, 'span').text
                K = Upper_K + "_" + Lower_K
                if K == "_":
                    K = ""
                Upper_L = columns[11].find_element(By.TAG_NAME, 'div').text
                Lower_L = columns[11].find_element(By.TAG_NAME, 'span').text
                L = Upper_L + "_" + Lower_L
                if L == "_":
                    L = ""
                Upper_M = columns[12].find_element(By.TAG_NAME, 'div').text
                Lower_M = columns[12].find_element(By.TAG_NAME, 'span').text
                M = Upper_M + "_" + Lower_M
                if M == "_":
                    M = ""
                Upper_N = columns[13].find_element(By.TAG_NAME, 'div').text
                Lower_N = columns[13].find_element(By.TAG_NAME, 'span').text
                N = Upper_N + "_" + Lower_N
                if N == "_":
                    N = ""
                Upper_O = columns[14].find_element(By.TAG_NAME, 'div').text
                Lower_O = columns[14].find_element(By.TAG_NAME, 'span').text
                O = Upper_O + "_" + Lower_O
                if O == "_":
                    O = ""
                Upper_P = columns[15].find_element(By.TAG_NAME, 'div').text
                Lower_P = columns[15].find_element(By.TAG_NAME, 'span').text
                P = Upper_P + "_" + Lower_P
                if P == "_":
                    P = ""
                Upper_Q = columns[16].find_element(By.TAG_NAME, 'div').text
                Lower_Q = columns[16].find_element(By.TAG_NAME, 'span').text
                Q = Upper_Q + "_" + Lower_Q
                if Q == "_":
                    Q = ""
                Upper_R = columns[17].find_element(By.TAG_NAME, 'div').text
                Lower_R = columns[17].find_element(By.TAG_NAME, 'span').text
                R = Upper_R + "_" + Lower_R
                if R == "_":
                    R = ""
                Upper_S = columns[18].find_element(By.TAG_NAME, 'div').text
                Lower_S = columns[18].find_element(By.TAG_NAME, 'span').text
                S = Upper_S + "_" + Lower_S
                if S == "_":
                    S = ""
                Upper_T = columns[19].find_element(By.TAG_NAME, 'div').text
                Lower_T = columns[19].find_element(By.TAG_NAME, 'span').text
                T = Upper_T + "_" + Lower_T
                if T == "_":
                    T = ""
                Upper_U = columns[20].find_element(By.TAG_NAME, 'div').text
                Lower_U = columns[20].find_element(By.TAG_NAME, 'span').text
                U = Upper_U + "_" + Lower_U
                if U == "_":
                    U = ""
                Upper_V = columns[21].find_element(By.TAG_NAME, 'div').text
                Lower_V = columns[21].find_element(By.TAG_NAME, 'span').text
                V = Upper_V + "_" + Lower_V
                if V == "_":
                    V = ""
                Upper_W = columns[22].find_element(By.TAG_NAME, 'div').text
                Lower_W = columns[22].find_element(By.TAG_NAME, 'span').text
                W = Upper_W + "_" + Lower_W
                if W == "_":
                    W = ""
                Upper_X = columns[23].find_element(By.TAG_NAME, 'div').text
                Lower_X = columns[23].find_element(By.TAG_NAME, 'span').text
                X = Upper_X + "_" + Lower_X
                if X == "_":
                    X = ""
                Upper_Y = columns[24].find_element(By.TAG_NAME, 'div').text
                Lower_Y = columns[24].find_element(By.TAG_NAME, 'span').text
                Y = Upper_Y + "_" + Lower_Y
                if Y == "_":
                    Y = ""
                Upper_Z = columns[25].find_element(By.TAG_NAME, 'div').text
                Lower_Z = columns[25].find_element(By.TAG_NAME, 'span').text
                Z = Upper_Z + "_" + Lower_Z
                if Z == "_":
                    Z = ""
                Upper_A1 = columns[26].find_element(By.TAG_NAME, 'div').text
                Lower_A1 = columns[26].find_element(By.TAG_NAME, 'span').text
                A1 = Upper_A1 + "_" + Lower_A1
                if A1 == "_":
                    A1 = ""
                Upper_B1 = columns[27].find_element(By.TAG_NAME, 'div').text
                Lower_B1 = columns[27].find_element(By.TAG_NAME, 'span').text
                B1 = Upper_B1 + "_" + Lower_B1
                if B1 == "_":
                    B1 = ""
                Upper_C1 = columns[28].find_element(By.TAG_NAME, 'div').text
                Lower_C1 = columns[28].find_element(By.TAG_NAME, 'span').text
                C1 = Upper_C1 + "_" + Lower_C1
                if C1 == "_":
                    C1 = ""
                Upper_D1 = columns[29].find_element(By.TAG_NAME, 'div').text
                Lower_D1 = columns[29].find_element(By.TAG_NAME, 'span').text
                D1= Upper_D1 + "_" + Lower_D1
                if D1 == "_":
                    D1 = ""
                Upper_E1 = columns[30].find_element(By.TAG_NAME, 'div').text
                Lower_E1 = columns[30].find_element(By.TAG_NAME, 'span').text
                E1 = Upper_E1 + "_" + Lower_E1
                if E1 == "_":
                    E1 = ""
                    
                Upper_F1 = columns[31].find_element(By.TAG_NAME, 'div').text
                Lower_F1 = columns[31].find_element(By.TAG_NAME, 'span').text
                F1 = Upper_F1 + "_" + Lower_F1
                if F1 == "_":
                    F1 = ""
                Upper_G1 = columns[32].find_element(By.TAG_NAME, 'div').text
                Lower_G1 = columns[32].find_element(By.TAG_NAME, 'span').text
                G1 = Upper_G1 + "_" + Lower_G1
                if G1 == "_":
                    G1 = ""
                Upper_H1 = columns[33].find_element(By.TAG_NAME, 'div').text
                Lower_H1 = columns[33].find_element(By.TAG_NAME, 'span').text
                H1 = Upper_H1 + "_" + Lower_H1
                if H1 == "_":
                    H1 = ""
                Upper_J1 = columns[34].find_element(By.TAG_NAME, 'div').text
                Lower_J1 = columns[34].find_element(By.TAG_NAME, 'span').text
                J1 = Upper_J1 + "_" + Lower_J1
                if J1 == "_":
                    J1 = ""
                Upper_K1 = columns[35].find_element(By.TAG_NAME, 'div').text
                Lower_K1 = columns[35].find_element(By.TAG_NAME, 'span').text
                K1 = Upper_K1 + "_" + Lower_K1
                if K1 == "_":
                    K1 = ""
                Upper_L1 = columns[36].find_element(By.TAG_NAME, 'div').text
                Lower_L1 = columns[36].find_element(By.TAG_NAME, 'span').text
                L1 = Upper_L1 + "_" + Lower_L1
                if L1 == "_":
                    L1 = ""
                Upper_M1 = columns[37].find_element(By.TAG_NAME, 'div').text
                Lower_M1 = columns[37].find_element(By.TAG_NAME, 'span').text
                M1 = Upper_M1 + "_" + Lower_M1
                if M1 == "_":
                    M1 = ""
                Upper_N1 = columns[38].find_element(By.TAG_NAME, 'div').text
                Lower_N1 = columns[38].find_element(By.TAG_NAME, 'span').text
                N1 = Upper_N1 + "_" + Lower_N1
                if N1 == "_":
                    N1 = ""
                    
            except:
                A = "none"  
                B = "none"  
                C = "none"  
                D = "none"  
                E = "none"  
                F = "none"  
                G = "none"  
                H = "none"  
                I = "none"  
                J = "none"  
                K = "none"  
                L = "none"  
                M = "none"  
                N = "none"  
                O = "none"  
                P = "none"  
                Q = "none"  
                R = "none"  
                S = "none"  
                T = "none"  
                U = "none"  
                V = "none"  
                W = "none"  
                X = "none"  
                Y = "none" 
                Z = "none"  
                A1 = "none"  
                B1 = "none"  
                C1 = "none"  
                D1 = "none"  
                E1 = "none" 
                
                F1 = "none"  
                G1 = "none"  
                H1 = "none"  
                J1 = "none"  
                K1 = "none"  
                L1 = "none"  
                M1 = "none"  
                N1 = "none" 
            A_list.append(A)
            B_list.append(B)
            C_list.append(C)
            D_list.append(D)
            E_list.append(E)
            F_list.append(F)
            G_list.append(G)
            H_list.append(H)
            I_list.append(I)
            J_list.append(J)
            K_list.append(K)
            L_list.append(L)
            M_list.append(M)
            N_list.append(N)
            O_list.append(O)
            P_list.append(P)
            Q_list.append(Q)
            R_list.append(R)
            S_list.append(S)
            T_list.append(T)
            U_list.append(U)
            V_list.append(V)
            W_list.append(W)
            X_list.append(X)
            Y_list.append(Y)
            Z_list.append(Z)
            A1_list.append(A1)
            B1_list.append(B1)
            C1_list.append(C1)
            D1_list.append(D1)
            E1_list.append(E1)
            
            F1_list.append(F1)
            G1_list.append(G1)
            H1_list.append(H1)
            J1_list.append(J1)
            K1_list.append(K1)
            L1_list.append(L1)
            M1_list.append(M1)
            N1_list.append(N1)
    try:
        A_list.remove('none')    
        B_list.remove('none')
        C_list.remove('none')
        D_list.remove('none')
        E_list.remove('none')
        F_list.remove('none')
        G_list.remove('none')
        H_list.remove('none')
        I_list.remove('none')
        J_list.remove('none')
        K_list.remove('none')
        L_list.remove('none')
        M_list.remove('none')
        N_list.remove('none')
        O_list.remove('none')
        P_list.remove('none')
        Q_list.remove('none')
        R_list.remove('none')
        S_list.remove('none')
        T_list.remove('none')
        U_list.remove('none')
        V_list.remove('none')
        W_list.remove('none')
        X_list.remove('none')
        Y_list.remove('none')
        Z_list.remove('none')
        A1_list.remove('none')
        B1_list.remove('none')
        C1_list.remove('none')
        D1_list.remove('none')
        E1_list.remove('none')
        
        F1_list.remove('none')
        G1_list.remove('none')
        H1_list.remove('none')
        J1_list.remove('none')
        K1_list.remove('none')
        L1_list.remove('none')
        M1_list.remove('none')
        N1_list.remove('none')
    except:
        pass   
    print(len(Player_list), len(A_list), len(B_list), len(C_list), len(D_list), len(E_list), len(F_list), len(G_list), len(H_list), len(I_list), len(J_list), len(K_list), len(L_list),
          len(M_list), len(N_list), len(O_list), len(P_list), len(Q_list), len(R_list), len(S_list), len(T_list), len(U_list),
           len(V_list), len(W_list), len(X_list), len(Y_list), len(Z_list), len(A1_list), len(B1_list), len(C1_list), len(D1_list), len(E1_list), len(F1_list), len(G1_list),
           len(H1_list), len(J1_list), len(K1_list), len(L1_list), len(M1_list), len(N1_list)) 
    dict = {'1': Player_list, '2': A_list, '3': B_list, '4': C_list, '5': D_list, '6': E_list, '7': F_list, '8': G_list, '9': H_list, '10': I_list, '11': J_list, '12': K_list,
            '13': L_list, '14': M_list, '15': N_list, '16': O_list, '17': P_list, '18': Q_list, '19': R_list, '20': S_list, '21': T_list, '22': U_list, '23': V_list, '24': W_list,
            '25': X_list, '26': Y_list, '27': Z_list, '28': A1_list, '29': B1_list, '30': C1_list, '31': D1_list, '32': E1_list, '33': F1_list, '34': G1_list, '35': H1_list, '36': J1_list,
            '37': K1_list, '38': L1_list, '39': M1_list, '40': N1_list}
    # dict = {'1': Player_list, '2': A_list, '3': B_list, '4': C_list, '5': D_list, '6': E_list, '7': F_list, '8': G_list, '9': H_list, '10': I_list, '11': J_list, '12': K_list,
    #         '13': L_list, '14': M_list, '15': N_list, '16': O_list, '17': P_list, '18': Q_list, '19': R_list, '20': S_list, '21': T_list, '22': U_list, '23': V_list, '24': W_list,
    #         '25': X_list, '26': Y_list, '27': Z_list, '28': A1_list, '29': B1_list, '30': C1_list, '31': D1_list, '32': E1_list}
    df = pd.DataFrame(dict)
    df.to_csv(f'Liverpool_teamtotal{season}.csv') 
    element1 = driver.find_element(By.XPATH, '//*[@id="statsFilter"]')
    actions = ActionChains(driver)
    actions.click(element1)  # Perform a click action on the element
    actions.key_down(Keys.DOWN)  # Press down the "down" key
    actions.key_up(Keys.DOWN)  # Press down the Control key (modify the key if needed)
    actions.key_down(Keys.ENTER)
    actions.key_up(Keys.ENTER)
    actions.perform()  # Perform the action
    l += 1
        


print('----------------finished-------------------')             

    
while True:
    pass