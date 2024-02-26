
# Hệ thống Quản lý Kho hàng 2
# SaurontheMighty

# Tạo các từ điển
đơn_giá = {}
mô_tả = {}
tồn_kho = {}

# Mở tệp chứa kho hàng
chi_tiết = open("stock.txt", "r")

# Dòng đầu tiên của tệp là số lượng mặt hàng
số_mặt_hàng  = int((chi_tiết.readline()).rstrip("\n"))

# Thêm mặt hàng vào các từ điển
for i in range(0, số_mặt_hàng):
    dòng  = (chi_tiết.readline()).rstrip("\n")
    x1, x2 = dòng.split("#")
    x1 = int(x1)
    x2 = float(x2)
    đơn_giá.update({x1: x2})

for i in range(0, số_mặt_hàng):
    dòng  = (chi_tiết.readline()).rstrip("\n")
    x1, x2 = dòng.split("#")
    x1 = int(x1)
    mô_tả.update({x1: x2})

for i in range(0, số_mặt_hàng):
    dòng  = (chi_tiết.readline()).rstrip("\n")
    x1, x2 = dòng.split("#")
    x1 = int(x1)
    x2 = int(x2)
    tồn_kho.update({x1: x2})

chi_tiết.close()

# Danh sách để lưu các mặt hàng đã mua
giỏ_hàng = []

c="y" # Chạy vòng lặp while cho đến khi người dùng muốn dừng lại

# Hướng dẫn
print("Chào mừng bạn đến với Hệ thống Quản lý Kho hàng")
print()
print("A-Thêm một mặt hàng")
print("R-Xóa một mặt hàng")
print("E-Chỉnh sửa chi tiết của một mặt hàng")
print("L-Liệt kê tất cả các mặt hàng")
print("I-Thăm dò thông tin về một mặt hàng")
print("P-Mua hàng")
print("C-Thanh toán")
print("S-Hiển thị tất cả các mặt hàng đã mua")
print("Q-Thoát")
print("remove-Xóa một mặt hàng khỏi giỏ hàng")
print("help-Xem tất cả các lệnh lại")
print()

tổng_chi_phí = 0 
cờ=0 # Để kiểm tra xem họ đã thanh toán chưa


while(c!= "q" or c!= "Q"):
    c= input("Bạn muốn làm gì? ")
    
    if(c=="q" or c=="Q"):
        break
        
    elif(c=="A" or c=="a"):#Thêm một mặt hàng
        p_no = int(input("Nhập số mặt hàng: "))
        p_pr = float(input("Nhập giá mặt hàng: "))
        p_desc = input("Nhập mô tả mặt hàng: ")
        p_stock = int(input("Nhập số lượng mặt hàng: "))
        
        m=0
        for i in range(0,len(đơn_giá)):
            if(p_no in đơn_giá):
                p_no+=1
                m=1
        if(m==1):
            print()
            print("Số mặt hàng đó đã tồn tại :(, đổi giá trị thành ",p_no)
                
        đơn_giá.update({p_no: p_pr})
        mô_tả.update({p_no: p_desc})
        if(p_stock > -1):
            tồn_kho.update({p_no: p_stock})
        else:
            p_stock = 0
            tồn_kho.update({p_no: p_stock})
            print("Tồn kho của một mặt hàng không thể là số âm, số lượng hàng tồn kho đã được đặt thành 0.")
        print()
        print("Số mặt hàng: ",p_no," Mô tả: ",mô_tả.get(p_no)," Giá: ",đơn_giá.get(p_no)," Tồn kho: ",tồn_kho.get(p_no))
        print("Mặt hàng đã được thêm thành công!")
        print()
        
    elif(c=="E" or c=="e"):#Chỉnh sửa một mặt hàng
        print()
        p_no = int(input("Nhập số mặt hàng: "))
        if(p_no in đơn_giá):
            p_pr = float(input("Nhập giá mặt hàng: "))
            p_desc = input("Nhập mô tả mặt hàng: ")
            p_stock = int(input("Nhập số lượng mặt hàng: "))
                
            đơn_giá.update({p_no: p_pr})
            mô_tả.update({p_no: p_desc})
            tồn_kho.update({p_no: p_stock})
            
        else:
            print("Mặt hàng đó không tồn tại, để thêm một mặt hàng sử dụng a")
        print()
    
            
    elif(c=="R" or c=="r"):#Xóa một mặt hàng
        print()
        p_no = int(input("Nhập số mặt hàng: "))
        if(p_no in đơn_giá):
            bạn_chắc_chắn = input("Bạn có chắc chắn muốn xóa mặt hàng đó không(y/n)? ")
            if(bạn_chắc_chắn=="y" or bạn_chắc_chắn=="Y"):
                đơn_giá.pop(p_no)
                mô_tả.pop(p_no)
                tồn_kho.pop(p_no)
                print("Mặt hàng đã được xóa thành công!")
            print()
        else:
            print("Xin lỗi, chúng tôi không có mặt hàng đó!")
            print()
        
    elif(c=="L" or c=="l"):#Liệt kê tất cả các mặt hàng
        print()
        print("Các mặt hàng và giá của chúng: ", đơn_giá)
        print("Mô tả: ", mô_tả)
        print("Tồn kho của mặt hàng: ", tồn_kho)
        print()

    
    elif(c=="I" or c=="i"):#Tìm hiểu về một mặt hàng
        print()
        p_no=int(input("Nhập số mặt hàng: "))
        if(p_no in đơn_giá):
            print()
            print("Số mặt hàng: ",p_no," Mô tả: ",mô_tả.get(p_no)," Giá: ",đơn_giá.get(p_no)," Tồn kho: ",tồn_kho.get(p_no))
            if(tồn_kho.get(p_no)<3 and tồn_kho.get(p_no)!=0):
                print("Chỉ còn ",tồn_kho.get(p_no)," sản phẩm! Nhanh lên!")
            print()
        else:
            print("Xin lỗi, chúng tôi không có mặt hàng đó!")
            print()
        
    elif(c=="P" or c=="p"):#Mua một mặt hàng
        print()
        p_no = int(input("Nhập số mặt hàng: "))
        if(p_no in đơn_giá):
            if(cờ==1):
                cờ=0
            tồn_kho_hiện_tại = tồn_kho.get(p_no)
            if(tồn_kho_hiện_tại>0):
                tồn_kho_hiện_tại = tồn_kho.get(p_no)
                tồn_kho[p_no] = tồn_kho_hiện_tại-1
                giá_mặt_hàng = đơn_giá.get(p_no)
                tổng_chi_phí = tổng_chi_phí+giá_mặt_hàng
                print(mô_tả.get(p_no),"đã được thêm vào giỏ hàng: ","$",giá_mặt_hàng)
                giỏ_hàng.append(p_no)#Lưu mặt hàng vào giỏ hàng
            else:
                print("Xin lỗi! Chúng tôi không có mặt hàng đó trong kho!")
        else:
                print("Xin lỗi! Chúng tôi không có mặt hàng đó!")
        print()
        
    elif(c=="C" or c=="c"):#Thanh toán
        print()
        print("Bạn đã mua các mặt hàng sau: ",giỏ_hàng)
        print("Tổng: ","$",round(tổng_chi_phí,2))
        thuế= round(0.13*tổng_chi_phí,2)
        print("Thuế là 13%: ","$",thuế)
        tổng = round(tổng_chi_phí+thuế,2)
        print("Sau Thuế: ","$",tổng)
        tổng_chi_phí=0
        cờ=1
        print()
        print("Bạn vẫn có thể mua các mặt hàng sau khi thanh toán, giỏ hàng của bạn đã được đặt lại. Để thoát nhấn q")
        print()
        
    elif(c=="help"):#Hiển thị tất cả các lệnh
        print()
        print("Trung tâm Trợ giúp")
        print("A-Thêm một mặt hàng")
        print("R-Xóa một mặt hàng")
        print("E-Chỉnh sửa thông tin của một mặt hàng")
        print("L-Liệt kê tất cả các mặt hàng")
        print("I-Thăm dò thông tin về một mặt hàng")
        print("P-Mua hàng")
        print("C-Thanh toán")
        print("S-Hiển thị tất cả các mặt hàng đã mua")
        print("remove-Xóa một mặt hàng khỏi giỏ hàng")
        print("help-Xem tất cả các lệnh lại")
        print("Nếu bạn có bất kỳ câu hỏi hoặc lo ngại khác, vui lòng liên hệ với quản lý.")
        print()

        
    elif(c=="remove" or c=="Remove"):#Để xóa một mặt hàng khỏi giỏ hàng
        print()
        bạn_chắc_chắn = input("Bạn có chắc chắn muốn xóa một mặt hàng khỏi giỏ hàng không(y/n)? ")
        if(bạn_chắc_chắn=="y"):
            p_no = int(input("Nhập số mặt hàng để xóa khỏi giỏ hàng: "))
            if(p_no in giỏ_hàng):
                tồn_kho_hiện_tại = tồn_kho.get(p_no)
                tồn_kho[p_no] = tồn_kho_hiện_tại+1
                giá_mặt_hàng = đơn_giá.get(p_no)
                tổng_chi_phí = tổng_chi_phí-giá_mặt_hàng
                j=0
                for i in range(0,len(giỏ_hàng)):#Tìm chỉ số của mặt hàng trong danh sách giỏ hàng
                    if(i==p_no):
                        j=i

                giỏ_hàng.pop(j)
                print(mô_tả.get(p_no),"đã được xóa khỏi giỏ hàng: ")
                print()
            else:
                print()
                print("Mặt hàng đó không có trong giỏ hàng của bạn!")
                print()
                
    elif(c=="s" or c=="S"):#in ra danh sách giỏ hàng
        print()
        print(giỏ_hàng)
        print()
        
    else:
        print()
        print("LỖI! Liên hệ quản lý để được trợ giúp!")
        print()


# Xuất tổng số tiền nếu người dùng thoát mà không thanh toán
if(tổng_chi_phí>0 and cờ==0):
    print()
    print("Bạn đã mua: ",giỏ_hàng)
    print("Tổng: ","$",round(tổng_chi_phí,2))
    thuế = round(0.13*tổng_chi_phí,2)
    print("Thuế là 13%: ","$",thuế)
    tổng = round(tổng_chi_phí+thuế,2)
    print("Sau Thuế: ","$",tổng)
    
print()
print("Cảm ơn bạn đã sử dụng IMS")

# Ghi dữ liệu kho hàng đã được cập nhật vào file
chi_tiết = open("stock.txt","w")
số_mặt_hàng=len(đơn_giá)
chi_tiết.write(str(số_mặt_hàng)+"\n")
for i in range(0,số_mặt_hàng):
    chi_tiết.write(str(i+1)+"#"+str(đơn_giá[i+1])+"\n")
    
for i in range(0,số_mặt_hàng):
    chi_tiết.write(str(i+1)+"#"+mô_tả[i+1]+"\n")
    
for i in range(0,số_mặt_hàng):
    chi_tiết.write(str(i+1)+"#"+str(tồn_kho[i+1])+"\n")
    
chi_tiết.close()
