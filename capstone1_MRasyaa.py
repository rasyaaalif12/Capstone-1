#=====================================================================================
## DATA UNIT GUDANG INVENTORY

stok_gudang=[
    {
        'kode': 'A001',
        'nama unit': 'Samsung Galaxy A55',
        'jumlah stok': 10,
        'harga': 6900000,
        'kategori': 'High-end',
        'deskripsi': '5G, 8GB/256GB, navy/lilac/iceblue'
    },  
    {    
        'kode': 'A002',
        'nama unit': 'Samsung Galaxy A35',
        'jumlah stok': 15,
        'harga': 5000000,
        'kategori': 'High-end',
        'deskripsi': '5G, 8GB/256GB, navy'
    }, 
    {
        'kode': 'A003',
        'nama unit': 'Samsung Galaxy A05',
        'jumlah stok': 9,
        'harga': 1500000,
        'kategori': 'Entry-level',
        'deskripsi': '4GB/64GB, light green'
    },
    {
        'kode': 'A004',
        'nama unit': 'Samsung Galaxy S24 Ultra C-VA',
        'jumlah stok': 12,
        'harga': 24000000,
        'kategori': 'Flagship',
        'deskripsi': '12GB/1TB, titanium black'
    }, 
    {
        'kode': 'A005',
        'nama unit': 'Samsung Galaxy Z Flip',
        'jumlah stok': 5,
        'harga': 10000000,
        'kategori': 'High-end',
        'deskripsi': '5G, 8GB/512GB, blue'
    }

    #ADD HERE  
]
    
stok_gudang1=stok_gudang.copy()
from tabulate import tabulate

#=====================================================================================
## 1. READ FUNCTION

def read_program():
    print('''
--------------MENAMPILKAN STOK INVENTORY-----------------

1. Menampilkan Seluruh Stok Unit Gudang
2. Menampilkan Salah Satu Stok Unit Gudang
3. Kembali ke Main Menu    
----------------------------------------------------------------   
''')
    option=input('Input (1/2/3): ')
    if option == '1':
        if len(stok_gudang1)==0:
            print('\n ****STOK UNIT TIDAK DITEMUKAN!****')
        else:
            print(tabulate(stok_gudang1, headers='keys', intfmt=',', tablefmt='psql' ))
            con_program()

    elif option == '2':
        if len(stok_gudang1)==0:
            print('\n ****STOK UNIT TIDAK DITEMUKAN!****')
        else:
            while True:
                kodeinput()
                for x, update in enumerate(stok_gudang1):
                    if update['kode']==kodeunit:
                        print(f'\t{x+1}. Kode Unit:{update['kode']}, Nama Unit:{update['nama unit']}, Jumlah Stok: {update['jumlah stok']}, Harga Unit: Rp.{update['harga']:,}, Kategori: {update['kategori']}')
                        con_program()                   
                if update['kode']!=kodeunit:
                    print('\n****KODE UNIT TIDAK DITEMUKAN!****')

    elif option == '3':
        mainmenu_program()
    else:
        print('\n****OPSI YANG ANDA INPUT SALAH!****')
        read_program()

#=====================================================================================
## 2. CREATE PROGRAM
def create_program():
    print('''
--------------MENAMBAHKAN STOK BARU PADA INVENTORY-----------------
1. Tambah Stok Unit Baru
2. Kembali ke Main Menu
-------------------------------------------------------------------    
''')
    option=input('Input (1/2): ')   
    if option == '1':
        while True: 
                kode=input('Input Kode Unit Baru (1 Alphabet & 3 Angka): ').upper()
                if len(kode)!=4:
                    print('\n****KODE UNIT BARU HARUS MENGGUNAKAN 1 ALPHABET & 3 ANGKA****')                                                
                elif kode[0].isalpha()==True and kode[1:4].isdigit()==True:
                    for update in stok_gudang1:
                        if update['kode']==kode:
                            print('****KODE UNIT SUDAH TERSEDIA!****')
                            break
                    else:
                        while True:            
                            nama2=input('Input Nama Unit Baru: ')
                            for x in nama2.split():
                                if x.isalnum():                         
                                    y=True
                                else:
                                    y=False
                                    break
                            if len(nama2)==0 or y==False:                
                                print('****ISI DATA UNIT DENGAN BENAR!****')
                            elif y==True:
                                break
                            else:
                                print('****ISI DATA UNIT DENGAN BENAR!****')                 

                        stock2={'jumlah stok': 0}
                        for a in stock2:
                            while True:
                                stock2[a]=input('Input Jumlah Stok: ')                   
                                if stock2[a].isdigit()!=True:
                                    print('****INPUT JUMLAH STOK DENGAN ANGKA!****')                       
                                elif (stock2[a].isdigit()==True):
                                    break      
                                else:
                                    print('****MASUKKAN INPUT DENGAN BENAR!****')

                        harga2={'harga': 0}
                        while True:
                            harga2['harga']=input('Input Harga Unit: ')
                            if harga2['harga'].isdigit()!=True:
                                print('****INPUT HARGA UNIT DENGAN ANGKA!****')
                            elif harga2['harga'].isdigit()==True:
                                harga2['harga']=int(harga2['harga'])
                                if harga2['harga']>=12000000:
                                    kategori= 'Flagship'
                                    break
                                elif harga2['harga']>=5000000:
                                    kategori= 'High-end'
                                    break
                                elif harga2['harga']>=3000000:
                                    kategori= 'Mid-range'
                                    break
                                elif harga2['harga']>=800000:
                                    kategori= 'Entry-level'
                                    break
                                else:
                                    kategori= 'Other'
                                    break
                            else:
                                print('****MASUKKAN INPUT DENGAN BENAR!****')                  
                        
                        while True:
                            desc=input('Input Deskripsi: ')
                            if len(desc)==0:                
                                print('****ISI DATA UNIT DENGAN BENAR!****')
                            elif len(desc)>0:
                                while True:    
                                    save2=input('Data Unit Akan Disimpan (Input Y untuk ya, Input N untuk tidak): ').upper()
                                    if save2=='Y':
                                        stok_gudang1.append(
                                        {
                                            'kode': kode,
                                            'nama unit': nama2, 
                                            'jumlah stok': int(stock2['jumlah stok']),
                                            'harga': int(harga2['harga']),
                                            'kategori': kategori,
                                            'deskripsi': desc
                                        }
                                        ) 
                                        print('****DATA TELAH TERSIMPAN!****')
                                        create_program()
                                    elif save2=='N':
                                        create_program()
                                    else:
                                        print('****OPSI YANG ANDA INPUT SALAH!****')
                            else:
                                print('****ISI DATA UNIT DENGAN BENAR!****')   
                else:
                    print('****MASUKKAN INPUT DENGAN BENAR!****')
 


#===========================================================================================
    elif option == '2':
        mainmenu_program()
    else:
        print('****OPSI YANG ANDA MASUKKAN SALAH!****')
        create_program()

#=====================================================================================
## 3. UPDATE PROGRAM
def update_program():
    print('''
--------------UPDATE STOK INVENTORY GUDANG-----------------
1. Update Stok Unit Tersedia
2. Kembali ke Main Menu  
-----------------------------------------------------------  
''')
    option=input('Input(1/2): ')
    while True:
        if option == '1':
            kodeinput()
            nomor_unit=kodeunit
            temp=''
            for update in stok_gudang1:
                if update['kode']==nomor_unit:

                    while True:
                        update_unit=input('Apakah Anda Akan Melanjutkan Update Data? (Input Y untuk ya, Input N untuk tidak): ').upper()
                        if update_unit=='Y':
                            
                            while True:
                                temp=input('Input Kolom yang Akan Diubah(kode/nama unit/jumlah stok/harga/deskripsi): ').lower()
                                if temp in stok_gudang1[0].keys():
                                    if temp == 'kode':
                                        while True:
                                            kode=input('Input Kode Unit Baru (1 Alphabet & 3 Angka): ').upper()                                            
                                            if len(kode)!=4:
                                                print('****KODE UNIT BARU HARUS MENGGUNAKAN 1 ALPHABET & 3 ANGKA****')
                                            elif kode[0].isalpha()==True and kode[1:4].isdigit()==True:
                                                for update in stok_gudang1:
                                                    if update['kode']==kode:
                                                        print('****KODE UNIT BARU TIDAK BOLEH SAMA DENGAN KODE UNIT LAMA****')
                                                        break
                                                if update['kode']!=kode:                                           
                                                    while True:
                                                        update_opt=input('Data Unit Akan Diperbaharui (Input Y untuk ya, Input N untuk tidak): ').upper()
                                                        if update_opt=='Y':
                                                            update[temp]=kode
                                                            print('****DATA TELAH DIPERBAHARUI!****')
                                                            con_program()
                                                        elif update_opt=='N':
                                                            update_program()
                                                        else:
                                                            print('****OPSI YANG ANDA MASUKKAN SALAH****')
                                            else:
                                                print('****MASUKKAN INPUT DENGAN BENAR!****')
# NAMA UNIT===============================================================================                                                       
                                    else:
                                        if temp == 'nama unit':
                                            while True:
                                                kode=input(f'Input {temp} Baru: ')
                                                for x in kode.split():
                                                    if x.isalnum():                         ## Name Checking
                                                        y=True
                                                    else:
                                                        y=False
                                                        break
                                                if len(kode)==0 or y==False:                
                                                    print('****ISI DATA UNIT DENGAN BENAR!****')
                                                elif y==True:
                                                    break
                                                else:
                                                    print('****ISI DATA UNIT DENGAN BENAR!****')

    ## AFTER FINISHED INPUTTING NAMA UNIT
                                            while True:
                                                update_opt=input('Data Unit Akan Diperbaharui (Input Y untuk ya, Input N untuk tidak): ').upper()
                                                if update_opt=='Y':
                                                    update[temp]=kode
                                                    print('****DATA TELAH DIPERBAHARUI!****')
                                                    con_program()
                                                elif update_opt=='N':
                                                    update_program()
                                                else:
                                                    print('****OPSI YANG ANDA MASUKKAN SALAH****')

# HARGA UNIT=============================================================================                                    
                                        else:
                                            if temp == 'harga':
                                                while True:
                                                    kode=input(f'Input {temp} Baru: ')
                                                    if (kode.isdigit()!=True):
                                                        print('****INPUT HARGA DENGAN ANGKA!****')
                                                    else:
                                                        if (kode.isdigit()==True):
                                                            kode=int(kode)
                                                            if kode>=12000000:
                                                                kategori= 'Flagship'
                                                        
                                                            elif kode>=5000000:
                                                                kategori= 'High-end'
                                                                
                                                            elif kode>=3000000:
                                                                kategori= 'Mid-range'
                                                                
                                                            elif kode>=800000:
                                                                kategori= 'Entry-level'
                                                                
                                                            else:
                                                                kategori= 'Other'

    ## AFTER FINISHED INPUTTING HARGA UNIT
                                                            while True:
                                                                update_opt=input('Data Unit Akan Diperbaharui (Input Y untuk ya, Input N untuk tidak): ').upper()
                                                                if update_opt=='Y':
                                                                    update[temp]=kode
                                                                    update['kategori']=kategori
                                                                    print('****DATA TELAH DIPERBAHARUI!****')
                                                                    con_program()
                                                                elif update_opt=='N': 
                                                                    update_program()
                                                                else:
                                                                    print('****OPSI YANG ANDA MASUKKAN SALAH****')
                                                        else:
                                                            print('****INPUT HARGA DENGAN ANGKA!****')

                                            else:
                                                if temp=='deskripsi':
                                                    while True:
                                                        desc=input(f'Input {temp} Baru: ')
                                                        if len(desc)==0:                
                                                            print('****ISI DATA UNIT DENGAN BENAR!****')
                                                        elif len(desc)>0:
                                                            break
                                                        else:
                                                            print('****ISI DATA UNIT!****')
                                                    
                                                    while True:
                                                        update_opt=input('Data Unit Akan Diperbaharui (Input Y untuk ya, Input N untuk tidak): ').upper()
                                                        if update_opt=='Y':
                                                            update[temp]=desc
                                                            print('****DATA TELAH DIPERBAHARUI!****')
                                                            con_program()
                                                        elif update_opt=='N':
                                                            update_program()
                                                        else:
                                                            print('****OPSI YANG ANDA MASUKKAN SALAH****')

# JUMLAH STOK=============================================================================                                    
                                                else:
                                                    if temp=='jumlah stok':
                                                        while True:
                                                            stock=input('Input Jumlah Stok yang akan Ditambah: ')
                                                            if stock.isdigit()!=True:
                                                                print('****INPUT JUMLAH STOK DENGAN ANGKA!****')
                                                            elif stock.isdigit()==True:
                                                                while True:    
                                                                    save=input(f'Anda Akan Menambah Jumlah Stok {update['kode']} Sejumlah {stock} Unit, Apakah Anda Ingin Melanjutkan? (Input Y untuk ya, Input N untuk tidak): ').upper()
                                                                    if save=='Y':
                                                                        for n in stok_gudang: 
                                                                            if n in stok_gudang1:
                                                                                update['jumlah stok']+=int(stock)
                                                                                break
                                                                            else:
                                                                                update['jumlah stok']=int(stock)
                                                                                break
                                                                        print('****DATA BERHASIL DISIMPAN!****')
                                                                        con_program()
                                else:
                                    print('****OPSI YANG ANDA MASUKKAN SALAH****')
                        elif update_unit=='N':
                            update_program()
                        else:
                            print('****OPSI YANG ANDA MASUKKAN SALAH!****')                               
            if temp!='kode':
                if update['kode']!=nomor_unit:
                    print('****UNIT TIDAK DITEMUKAN!****')
                
        elif option == '2':
            mainmenu_program()
        else:
            print('****OPSI YANG ANDA MASUKKAN SALAH!****')
            update_program()


#=====================================================================================
## 4. DELETE FUNCTION
def delete_program():
    print('''
--------------MENGHAPUS STOK INVENTORY GUDANG-----------------

1. Menghapus Jumlah Stok Unit
2. Menghapus Unit
3. Pembersihan Gudang
4. Kembali ke Main Menu              
--------------------------------------------------------------
''')
    option=input('Input (1/2/3/4): ')
    if option=='1':
        for update in stok_gudang1:
            while True:
                print('****INPUT KODE UNIT YANG AKAN DIHAPUS****')
                kodeinput()
                for update in stok_gudang1:
                    if update['kode']==kodeunit:
                        print('****ANDA AKAN MENGURANGI JUMLAH UNIT PADA STOK YANG SUDAH TERSEDIA****')
                        stock1={'jumlah stok': update['jumlah stok']}
                        
                        while True:
                            stock=input('Input Jumlah Stok yang akan Dihapus: ')
                            if int(stock)>update['jumlah stok']:
                                print('****INPUT MELEBIHI JUMLAH STOK TERSEDIA****')
                            elif stock.isdigit()!=True:
                                print('****INPUT JUMLAH STOK DENGAN ANGKA!****')
                            elif stock.isdigit()==True:
                                while True:    
                                    save=input(f'Anda Akan Mengurangi Jumlah Stok {update['kode']} Sejumlah {stock} Unit, Apakah Anda Ingin Melanjutkan? (Input Y untuk ya, Input N untuk tidak): ').upper()
                                    if save=='Y':
                                        for n in stok_gudang: 
                                            if n in stok_gudang1:
                                                update['jumlah stok']-=int(stock)
                                                break
                                            else:
                                                update['jumlah stok']=int(stock)
                                                break
                                        print('****DATA BERHASIL DISIMPAN!****')
                                        con_program()
                                    elif save=='N':
                                        delete_program()
                                    else:
                                        print('****OPSI YANG ANDA MASUKKAN SALAH!****')
                            else:
                                print('****MASUKKAN INPUT DENGAN BENAR!****')            
                if update['kode']!=kodeunit:
                    print('****UNIT TIDAK DITEMUKAN!****')
                else:
                    print('****UNIT TIDAK DITEMUKAN!****')

    elif option=='2':
        while True:
            print('****INPUT KODE UNIT YANG AKAN DIHAPUS****')
            kodeinput()
            for update in stok_gudang1:
                if update['kode']==kodeunit:
                    while True:
                        delete_kode=input(f'Anda Akan Menghapus Daftar Unit Dengan Kode Unit: {update['kode']}, Apakah Anda Ingin Melanjutkan? (Input Y untuk ya, Input N untuk tidak): ').upper()
                        if delete_kode=='Y':
                            for i in range(len(stok_gudang1)):
                                if stok_gudang1[i]['kode']==update['kode']:
                                    del stok_gudang1[i]
                                    print('****DATA UNIT TELAH TERHAPUS!****')
                                    con_program()
                        elif delete_kode=='N':
                            delete_program()
                        else:
                            print('****OPSI YANG ANDA MASUKKAN SALAH!****')
            if update['kode']!=kodeunit:
                print('****UNIT TIDAK DITEMUKAN!****')


    elif option=='3':
        while True:
            print('****ANDA AKAN MEMBERSIHKAN SELURUH GUDANG, APA ANDA YAKIN?****')
            clear_opt=input('INPUT Y UNTUK YA, INPUT N UNTUK TIDAK: ').upper()
            if clear_opt=='Y':
                if len(stok_gudang1)==0:
                    print('****STOK UNIT TIDAK DITEMUKAN!****')
                    con_program()
                elif len(stok_gudang1)!=0:
                    while True:
                        password_program()
                        print('****SELURUH GUDANG TELAH DIBERSIHKAN!****')
                        stok_gudang1.clear()
                        con_program()
            elif clear_opt=='N':
                delete_program()
            else:
                print('****OPSI YANG ANDA MASUKKAN SALAH!****')

    elif option=='4':
        mainmenu_program()
    else:
        print('****OPSI YANG ANDA MASUKKAN SALAH!****')
        delete_program()


#=====================================================================================
## 5. QUIT FUNCTION
def quit_program():
    print('****Terima Kasih Telah Menggunakan Aplikasi****')
    quit()


#=====================================================================================
### MAIN MENU FUNCTION
def mainmenu_program():
    print('''
    ---------------------------------------------
        GUDANG INVENTORY MANAGEMENT PROGRAM
                    MAIN MENU
    1. Menampilkan stok inventory
    2. Menambah stok inventory
    3. Update stok inventory
    4. Menghapus stok inventory
    5. Keluar dari program
    ---------------------------------------------
''')
    option=input('Input (1/2/3/4/5): ')
    if option == '1':
        read_program()
    elif option == '2':
        create_program()
    elif option == '3':
        update_program()
    elif option == '4':
        delete_program()
    elif option == '5':
        quit_program()
    else:
        print('\n ****INPUT YANG ANDA MASUKKAN SALAH!****')
        mainmenu_program()

#=======================================================================================
### KODE UNIT
### Input Kode Unit With Loops------------------------------------------------------
def kodeinput():
    while True:
        global kodeunit
        print(tabulate(stok_gudang1, headers='keys', intfmt=',', tablefmt='psql' ))
       
        kodeunit=input('Input Kode Unit (Input "B" Untuk Kembali ke Main Menu): ').upper()
        if kodeunit=='B':
            mainmenu_program()
        elif len(stok_gudang1)==0:
            print('****KODE UNIT TIDAK DITEMUKAN!****')
        elif kodeunit.isalnum()==True and kodeunit!='B':
            break
        else:
            print('****KODE UNIT TIDAK DITEMUKAN!****')

### Input to Main Menu--------------------------------------------------------------
def kodeinput2():
    while True:
        global kodeunit
        kodeunit=input('Input "B" Untuk Kembali ke Main Menu: ').upper()
        if kodeunit=='B':
            mainmenu_program()
        else:
            print('****INPUT YANG ANDA MASUKKAN SALAH!****')

### Input Kode Without Loops---------------------------------------------------------
def kodeinput3():
    while True:
        global kodeunit
        kodeunit=input('Input Kode Unit (Input "B" Untuk Kembali ke Main Menu): ').upper()
        if kodeunit=='B':
            mainmenu_program()
        elif len(stok_gudang1)==0:
            print('****KODE UNIT TIDAK DITEMUKAN!****')
        elif kodeunit.isalnum()==True and kodeunit!='B':
            break
        else:
            print('****KODE UNIT TIDAK DITEMUKAN!****')

#==========================================================================================
### CONTINUE FUNCTION
def con_program():
    while True:
        con_option=input('Tekan B Untuk Kembali ke Main Menu, Tekan Q Untuk Akhiri Program: ').upper()
        if con_option == 'B':
            mainmenu_program()
        elif con_option == 'Q':
            quit_program()
        else:
            print('****INPUT YANG ANDA MASUKKAN SALAH!****')

#===========================================================================================
### ADMIN ACCESS FUNCTION
def password_program():
    print('****INPUT PASSWORD ADMIN****')
    admin_access='167439'
    for i in range(6):
        i+=1
        admin_pass=input('Input Password Admin: ')
        if admin_pass==admin_access:
            print('****PASSWORD BERHASIL DIINPUT!****')
            break
        else:
            while True:
                if admin_pass!=admin_access:
                    if i>0 and i<=5:
                        print(f'****PASSWORD ADMIN SALAH! SILAKAN COBA LAGI ({6-i})****')
                        break
                    else:
                        print('****PASSWORD ADMIN SALAH! KEMBALI KE MAIN MENU****')
                        mainmenu_program()

#===========================================================================================
### ENTER PROGRAM
mainmenu_program()
