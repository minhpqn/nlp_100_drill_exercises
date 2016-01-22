# Chương 4: Morphological Analysis trong tiếng Nhật (形態素解析)

## Xử lý text với MeCab

Chuyển vào thư mục có chứa file neko.txt và thực hiện lệnh sau.
    mecab neko.txt -o neko.txt.mecab

## Cách đọc các câu từ file kết quả morphological analysis
Đầu vào là kết quả morphological analysis bởi tool MeCab. Đọc file kết quả và trả về danh sách các sentences.

Thuật toán:
- Mở file để đọc
- Khởi tạo danh sách câu; Khởi tạo danh sách morphemes;
- Đọc từng dòng trong file: 1) Nếu dòng khác EOS, đọc thông tin của morphome; 2) Nếu là dòng EOS => Lưu danh sách morphomes vào câu và khởi tạo lại danh sách morphemes.



