100 bài luyện tập xử lý ngôn ngữ tự nhiên
=========================================

Dịch từ tài liệu [言語処理100本ノック](<http://www.cl.ecei.tohoku.ac.jp/nlp100>) của lab Inui-Okazaki, đại học Tohoku, Nhật Bản. Người dịch: Phạm Quang Nhật Minh
(minhpqn).

Tham khảo thêm phiên bản cũ của tài liệu tại [NLP 100 Drill
Exercises](<http://www.cl.ecei.tohoku.ac.jp/index.php?NLP%20100%20Drill%20Exercises#x3adf301>)

Chú ý: Khi sử dụng tài liệu 100 bài luyện tập xử lý ngôn ngữ tự nhiên, cần trích dẫn các nguồn sau: 

- Tài liệu "言語処理100本ノック" của lab Inui-Okazaki, đại
học Tohoku, Nhật Bản. URL: <http://www.cl.ecei.tohoku.ac.jp/nlp100> 
- Đường link tới bản dịch hiện tại: <https://github.com/minhpqn/nlp_100_drill_exercises>. Người dịch: Phạm Quang Nhật Minh.

## Chương 1: Bài tập khởi động

### 00. Đảo ngược xâu ký tự

Hãy đảo ngược xâu ký tự "stressed" (theo thứ tự từ cuối xâu đến đầu xâu ký tự).

### 01. Trích xuất ký tự từ xâu ký tự

Từ xâu ký tự "MPyaktQrBoilk RCSahr", hãy trích xuất các ký tự ở vị trí
2,4,6,8,10,12,14,16,18,20 và kết hợp theo thứ tự đó để tạo thành 1 xâu ký tự mới
(ký tự space cũng được tính, các ký tự được đánh số từ 1).

### 02. Kết hợp hai xâu ký tự

Hãy kết hợp hai xâu ký tự "Partrol" và "Car" để tạo thành xâu mới "PatrolCar".

### 03. Tokenize và thống kê số lượng ký tự của mỗi từ

1.  Tokenize câu sau: "Now I need a drink, alcoholic of course, after the heavy
    lectures involving quantum mechanics."

2.  Đưa ra danh sách gồm số ký tự alphabet trong mỗi từ theo thứ tự xuất hiện
    của từ đó trong câu.

### 04. Ký tự thành phần

1.  Tokenize câu sau: "Hi He Lied Because Boron Could Not Oxidize Fluorine. New
    Nations Might Also Sign Peace Security Clause. Arthur King Can."

2.  Lấy ra ký tự đầu tiên của các từ ở vị trí 1, 5, 6, 7, 8, 9, 15, 16, 19; với
    các từ còn lại lấy ra 2 ký tự đầu tiên. Tạo ra một map từ các xâu ký tự được
    trích ra tới vị trí của từ trong câu.

### 05. n-gram

1.  Viết hàm sinh ra tất cả các n-gram từ một dãy cho trước (xâu ký tự hoặc danh
    sách).

2.  Sử dụng hàm đã viết, sinh ra word bi-gram và character bi-gram từ câu sau:
    "I am an NLPer"

### 06. Tập hợp

1.  Sinh ra tập X và Y tương ứng là tập các character bi-gram từ hai xâu ký tự
    "paraparaparadise" và "paragraph".

2.  Sinh ra các tập hợp union, intersection và difference của X và Y

3.  Kiểm tra xem bi-gram 'se' có thuộc tập X (Y) hay không?

### 07. Sinh ra câu từ template

Viết hàm số nhận vào 3 biến x, y, z và trả về xâu ký tự "y vào lúc x giờ là z"
Sinh ra kết quả với các giá trị x, y, z sau đây x="12" y="Nhiệt độ" z=22.4

### 08. Xâu mật mã

Từ các ký tự của một xâu cho trước, cài đặt hàm có tên cipher để mã hoá xâu như
sau: - Nếu là ký tự tiếng Anh ở dạng thường (lower-case characters) thì chuyển
thành ký tự có mã là (219 - mã ký tự). - Các ký tự khác giữ nguyên.

Sử dụng hàm đã viết để mã hoá và giải mã các xâu ký tự tiếng Anh.

### 09. [Typoglycemia](<https://en.wikipedia.org/wiki/Typoglycemia>)

Cho đầu vào là một câu tiếng Anh bao gồm các word ngăn cách nhau bằng ký tự
space. Viết chương trình thực hiện việc sau: - Với mỗi word, giữ nguyên ký tự
đầu và ký tự cuối, đảo thứ tự một cách ngẫu nhiên các ký tự còn lại của (tất
nhiên các word có ít hơn 4 ký tự thì không cần làm gì) - Cho trước một câu tiếng
Anh hợp lệ, ví dụ "I couldn't believe that I could actually understand what I
was reading : the phenomenal power of the human mind .", chạy chương trình đã
viết để đưa ra kết quả.

## Chương 2: Các lệnh cơ bản trên môi trường Unix

Các bài tập trong chương này sử dụng dữ liệu trong file
[hightemp.txt](<http://www.cl.ecei.tohoku.ac.jp/nlp100/data/hightemp.txt>). File
này bao gồm các bản ghi nhiệt độ cao nhất ở Nhật Bản. Mỗi bản ghi bao gồm 3 cột
"Tỉnh", "Địa điểm", "Nhiệt độ" (độ C), và ngày tháng đo. Các cột dữ liệu được
phân cách bằng ký tự tab. Viết các chương trình thực hiện các nhiệm vụ trong các
bài tập dưới đây. Sau đó, chỉ sử dụng các lệnh trong unix để thực hiện các nhiệm
vụ đó và xác nhận xem kết quả của chương trình bạn viết có giống với kết quả các
lệnh unix đưa ra hay không.

### 10. Đếm số dòng trong file

Đếm số dòng trong file. Xác nhận kết quả bằng lệnh wc trong unix.

### 11. Biến đổi các ký tự tab thành space

Chuyễn mỗi ký tự tab thành ký tự space. Xác nhận kết quả lần lượt bằng các lệnh
sed, tr, và expand.

### 12. Lưu cột 1 vào file col1.txt, cột 2 vào file col2.txt

Trích xuất nội dung trong cột 1, cột 2 và lưu vào các file tương ứng: col1.txt
và col2.txt. Thử thực hiện công việc chỉ dùng lệnh cut trong unix.

### 13. Trộn hai file col1.txt và col2.txt

Kết hợp nội dung trong 2 file col1.txt và col2.txt để tạo thành một file mới có
nội dung giống với cột 1 và cột 2 trong file ban đầu (các cột cách nhau bởi ký
tự tab). Sử dụng lệnh paste để thực hiện bài tập và xác nhận kết quả của chương
trình bạn viết.

### 14. Trích xuất ra N hàng đầu tiên của file

Viết chương trình trích xuất ra N hàng đầu tiên của file. Biến số dạng dòng lệnh
là số tự nhiên N. Sử dụng lệnh head trong unix để thực hiện công việc.

### 15. Trích xuất ra N hàng cuối cùng của file

Viết chương trình trích xuất ra N hàng cuối cùng của file. Chương trình nhận đầu
vào từ dòng lệnh là số tự nhiên N. Sử dụng lệnh tail trong unix để thực hiện
công việc.

### 16. Chia file thành N phần

Chia file thành các files nhỏ với N lines mỗi file (đơn vị là các hàng trong
file). Chương trình nhận đầu vào từ dòng lệnh là số tự nhiên N. Sử dụng lệnh
split để thực hiện công việc (split -l N).

Sau đó, cải tiến chương trình để chia file thành thành N phần bằng nhau (thay vì
N lines mỗi file).

### 17. Đưa ra các các xâu ký tự duy nhất (unique) trong cột 1

Đưa ra các xâu ký tự duy nhất trong cột 1 của file. Sử dụng lệnh cut, sort, uniq
để thực hiện nhiệm vụ.

### 18. Sắp xếp các hàng theo thứ tự giảm dần của giá trị (numeric value) của cột thứ 3

Viết chương trình thực hiện nhiệm vụ trên. Dùng lệnh sort để xác nhận (trong bài
tập này, kết quả của chương trình của bạn với lệnh sort có thể khác nhau do có
thể có các giá trị giống nhau trong cột thứ 3).

### 19. Sắp xếp theo tần suất xuất hiện

Đưa ra tần suất xuất hiện của các giá trị trong cột 1; sắp xếp các giá trị trong
cột 1 theo thứ tự từ cao đến thấp của tần suất xuất hiện. Chỉ dùng lệnh cut,
uniq, sort để thực hiện nhiệm vụ.

## Chương 3: Biểu thức chính quy (regular expressions)

Bài tập trong chương 3 sử dụng file
[jawiki-country.json.gz](<http://www.cl.ecei.tohoku.ac.jp/nlp100/data/jawiki-country.json.gz>).
File này lưu trữ các tài liệu Wikipedia và có định dạng sau đây. - Dòng thứ nhất
lưu trữ thông tin về tài liệu dưới định dạng JSON. - Ở các dòng tiếp theo, dòng
tiêu đề của văn bản được lưu trữ tại khoá "title"; nội dung của tài liệu được
lưu trữ tại khoá "text". Các dòng này được lưu trữ ở định dạng JSON.

Lập trình để xử lý các việc sau đây.

### 20. Đọc vào dữ liệu JSON

Đọc dữ liệu từ file JSON chứa các tài liệu Wikipedia, trích xuất & hiển thị nội
dung của tài liệu (trường text của JSON object) có liên quan đến "イギリス" (có
nghĩa là nước Anh). Sử dụng các nội dung của tài liệu được trích xuất này để
thực thi các nhiệm vụ trong các bài tập từ 21-29.

### 21. Trích xuất các dòng có chứa tên đề mục

Trong các tài liệu, trích xuất các dòng có chứa tên đề mục (category name hay
カテゴリ名).

### 22. Trích xuất các tên đề mục (Category name)

Trích xuất tên đề mục của trong các tài liệu. Trong bài tập này, cần trích xuất
chính xác các tên đề mục chứ không phải dòng chứa tên đề mục.

### 23. Cấu trúc của các Section

Hiển thị tên của các section và level của các section trong các tài liệu
Wikipedia (Ví dụ với section == Section Name ==" thì level bằng 1)

### 24. Trích xuất các liên kết file

Trích xuất toàn bộ các liên kết đến các media files trong tài liệu.

### 25. Trích xuất templates

Trích xuất vị trí và tên các folder có template "基礎情報" trong tài liệu. Lưu
kết quả trong các đối tượng dictionary. Tham khảo về templates tại
[đây](<https://en.wikipedia.org/wiki/Help:Infobox>).

### 26. Loại bỏ các emphasis markups

Trong khi làm các xử lý ở bài tập 25, xoá các emphasis markup (italic, bold,
both) từ vị trí của các templates và biến đổi thành plain text. (Tham khảo về
các loại markup tại [Wiki
markup](<https://en.wikipedia.org/wiki/Help:Cheatsheet>), bảng tham khảo bằng
tiếng Nhật tại
[マークアップ早見表](<http://ja.wikipedia.org/wiki/Help:%E6%97%A9%E8%A6%8B%E8%A1%A8>)).

### 27. Xoá các link đến các trang Wikipedia khác

Nhiệm vụ giống như bài 26 và thêm vào xử lý sau. Xoá các markups của liên kết
đến các trang Wikipedia khác từ các templates được trích xuất và biến đổi thành
dạng text. (Tham khảo về các loại markup tại [Wiki
markup](<https://en.wikipedia.org/wiki/Help:Cheatsheet>), bảng tham khảo bằng
tiếng Nhật tại
[マークアップ早見表](<http://ja.wikipedia.org/wiki/Help:%E6%97%A9%E8%A6%8B%E8%A1%A8>)).

### 28. Xoá các markup trong văn bản

Thêm vào xử lý ở bài 27. Xoá các markup trong các templates càng nhiều càng tốt
và in ra các thông tin cơ bản về quốc gia.

### 29. Lấy ra các URL của quốc kỳ

Sử dụng nội dung của các template và lấy ra URl đến quốc kỳ (国旗画像のURL).
Hint: Gọi API [imageinfo](<https://www.mediawiki.org/wiki/API:Imageinfo>) của
[MediaWWiki](<https://www.mediawiki.org/wiki/API:Main_page>), biến đổi các file
references thành URL.

## Chương 4: Morphological Analysis trong tiếng Nhật (形態素解析)

Download file [neko.txt](<http://www.cl.ecei.tohoku.ac.jp/nlp100/data/neko.txt>)
là nội dung bằng plain text của cuốn tiểu thuyết "吾輩は猫である" của nhà văn
夏目漱石 (Soseki Natsume).

Sử dụng package [MeCab](<http://taku910.github.io/mecab/>) để thực hiện
"morphological analysis" (Tham khảo trang tiếng Nhật tại
[đây](<https://ja.wikipedia.org/wiki/%E5%BD%A2%E6%85%8B%E7%B4%A0%E8%A7%A3%E6%9E%90>)).
Lưu kết quả vào file neko.txt.mecab. Sử dụng file kết quả để thực hiện các công
việc ở các bài tập dưới đây.

Chú ý: Trong các bài tập 37, 38, 39 có thể sử dụng các phần mềm
[matplitlib](<http://matplotlib.org/>) hoặc
[Gnuplot](<http://www.gnuplot.info/>).

@All: Với các bạn không quen xử lý text tiếng Nhật, có thể dùng một file text
tiếng Anh và thực hiện POS tagging, sau đó làm các bài tập dưới đây.

### 30. Đọc vào kết quả morphological analysis

Viết chương trình đọc vào kết quả morphological analysis (file neko.txt.mecab).

Yêu cầu: Với mỗi morpheme, lưu các thông tin: 表層形 (surface form), 基本形
(base form), 品詞 (pos), 品詞細分類1 (pos1) bằng cấu trúc dữ liệu hash map với
các key tương ứng là: surface, base, pos, pos1. Lưu trữ mỗi câu bằng danh sách
của các morpheme. Trong các bài tập còn lại trong chương 4, hãy sử dụng cách tổ
chức dữ liệu trong bài 30 này.

### 31. Động từ

Trích xuất tất cả các surface forms của động từ (pos=動詞).

### 32. Dạng nguyên thể của động từ (動詞の原形)

Trích xuất tất cả dạng nguyên thể của động từ (base form).

### 33. Danh từ dạng サ (サ変名詞)

Trích xuất toàn bộ các danh từ dạng サ (サ変名詞). Tham khảo trang Wikipedia
tiếng Nhật về
[サ行変格活用](<https://ja.wikipedia.org/wiki/%E3%82%B5%E8%A1%8C%E5%A4%89%E6%A0%BC%E6%B4%BB%E7%94%A8>).

### 34. 「AのB」

Trích xuất tất cả các danh từ ghép (compound nouns) gồm 2 danh từ kết nối bằng
の.

### 35. Trích xuất các kết nối danh từ (noun connections hay 名詞の連接)

Trích xuất tất cả các noun connections (các danh từ đứng cạnh nhau liên tiếp).
Khi trích xuất, chú ý trích xuất chuỗi danh từ matching dài nhất có thể. Ví dụ
ABC trong đó A, B, C là danh từ thì phải trích xuất ABC thay vì AB.

### 36. Tần suất xuất hiện của từ

Lập trình tính tần suất xuất hiện của từ trong văn bản. Đưa ra các từ theo thứ
tự giảm dần của tần suất xuất hiện.

### 37. Top 10 từ xuất hiện nhiều nhất

Vẽ đồ thị (ví dụ bar graph) của tần suất xuất hiện của 10 từ xuất hiện nhiều
nhất trong văn bản.

### 38. Histogram

Vẽ đồ thị histogram tần suất xuất hiện của các từ. Trục ngang là tần suất xuất
hiện. Trục dọc là các từ.

### 39. Luật Zipf

Vẽ đồ thị với trục ngang là rank của các từ theo tần suất xuất hiện (cao đến
thấp), trục dọc là tần suất xuất hiện của các từ.

## Chương 5: Dependency parsing (係り受け解析)

Thực hiện phân tích cấu trúc ngữ pháp (dependency parsing) bằng công cụ
[CaboCha](<http://taku910.github.io/cabocha/>) cho file
[neko.txt](<http://www.cl.ecei.tohoku.ac.jp/nlp100/data/neko.txt>) và lưu kết
quả vào file neko.txt.cabocha. Sử dụng file kết quả này làm đầu vào cho các bài
tập dưới đây.

### 40. Đọc vào kết quả dependency parsing (theo morphemes)

Cài đặt lớp Morph cho các morphemes. Lớp này có các biến thành phần (member
variables) là surface (cho surface forms của morphems), base (cho base form),
pos (cho POS tag), pos1 (cho detailed POS tag 1 品詞細分類1). Sau đó đọc vào kết
quả phân tích dependency parsing trong file neko.txt.cabocha. Mỗi câu sẽ bao gồm
một danh sách các Morph objects. Hiển thị danh sách các morphemes cho câu thứ 3
trong văn bản.

### 41. Đọc vào kết quả dependency parsing (theo chunks và depedency relations)

Tiếp theo bài 40, cài đặt lớp Chunk để lưu trữ các chunk (hay bunsetsu (文節)).
Lớp này có các biến thành phần là: - morphs (để lưu trữ danh sách các Morph
objects) - dst để lưu trữ index của chunk mà chunk hiện tại trỏ đến (chunk đích - destination) - srcs để lưu trữ danh sách các indexes của các chunk trỏ đến chunk hiện tại.

Sau đó, đọc vào kết quả dependency parsing. Mỗi câu sẽ bao gồm danh sách của các
Chunk objects. Hiển thị xâu ký tự và giá trị của biến dst của các chunk trong câu
thứ 8 của file đầu vào.

Các bài tập còn lại trong chương 5 sẽ sử dụng các chương trình được tạo ra
trong bài tập 40 và 41.

### 42. Hiển thị chunk nguồn (head) và chunk đích (modifier) trong các depedency relations

Hiển thị nội dung (dạng text) các chunk nguồn (head) và chunk đích (modifier)
trên mỗi dòng và cách nhau bởi ký tự tab. Chú ý không hiển thị các dấu
(punctuation marks) trong các chunk.

### 43. Trích xuất các dependency relations giữa các chunk chứa danh từ và các chunk chứa động từ

Trích xuất các dependency relations giữa các chunk chứa danh từ và các chunk
chứa động từ. In ra theo định dạng tab. Tương tự như bài 42, không hiển thị các
dấu (punctuation marks) trong các chunk.

### 44. Visualize cây dependency

Visualize dependency trees của một câu cho trước. Khi visualize, biến các
dependency trees theo [ngôn ngữ
DOT](<https://en.wikipedia.org/wiki/DOT_%28graph_description_language%29>), hay
sử dụng [Graphviz](<http://www.graphviz.org/>). Nếu sử dụng Python, có thể hiển
thị đồ thị có hướng bằng thư viện/package
[pydot](<https://code.google.com/p/pydot/>).

### 45. Trích xuất các verb case patterns

Yêu cầu của bài tập này là tìm hiểu (investigate) về case frame trong tiếng Nhật
sử dụng dữ liệu trong file đầu vào neko.txt. Coi các động từ là vị ngữ
(predicate), các trợ từ (như が,を,...) của chunk liên với với động từ là các case, hãy
in ra các động từ và các "case" theo định dạng cách nhau bởi ký tự tab. Output
của chương trình cần thoả mãn các điều kiện sau: 

- Các vị ngữ là dạng nguyên thể
(base form) của động từ, tính từ bên trái nhất (lef-most) của các chunk
(bunsetsu). 
- Coi các trợ từ liên kết với các vị ngữ là các "case" trong case
frame. 
- Nếu một vị ngữ được liên kết bởi nhiều trợ từ, in tất cả các trợ từ
theo thứ tự từ điển. Các trợ từ cách nhau bởi dấu cách

Xem xét ví dụ sau: 「吾輩はここで始めて人間というものを見た」(câu thứ 8 trong
file neko.txt.cabocha). Câu này gồm hai động từ 始める và 見る. Nếu trong kết
quả phân tích cú pháp, động từ 始める liên kết với chunk ここで, động từ 見る
liên kết với với chunk 吾輩は và ものを, chương trình sẽ in ra:

```
始める で
見る は を
```

Lưu output của chương trình ra file, xác nhận các mục sau chỉ với các lệnh của Unix.

-   Kết hợp các động từ xuất hiện trong corpus và các case patterns
-   Các case patterns của các động từ する, 見る, 与える (theo thứ tự từ cao đến thấp của tần suất xuất hiện trong corpus).

Tham khảo về case frame structures trong tiếng Nhật tại
[đây](<http://www.aclweb.org/anthology/C00-1063>) (Kawahara et al., 2010).

### 46. Trích xuất thông tin của case frames của các động từ

Chỉnh sửa bài tập 45, trích xuất thêm các chunks mà các vị ngữ (predicate) liên
kết tới. In ra theo định dạng tab. Ngoài các điều kiện đưa ra ở bài tập 45,
output phải thoả mãn các điều kiện sau.

-   In ra các chunk (bunsetsu) ở dạng dãy các từ (không cần phải xoá đuôi và các
    trợ từ).

-   Trong trường hợp một predicates liên kết với nhiều chunk (bunsetsu), in ra
    các chunk này theo cùng thứ tự với các trợ từ. Dùng ký tự space giữa các
    chunk.

Xem xét ví dụ sau: 「吾輩はここで始めて人間というものを見た」(câu thứ 8 trong
file neko.txt.cabocha). Câu này gồm hai động từ 始める và 見る. Nếu trong kết
quả phân tích cú pháp, động từ 始める liên kết với chunk ここで, động từ 見る
liên kết với với chunk 吾輩は và ものを, chương trình sẽ in ra:

始める で ここで

見る は を 吾輩 ものを

### 47. Mining các cấu trúc câu có động từ chức năng

(cấu trúc này có tên tiếng Nhật là 機能動詞構文)

Bài tập này tập trung vào các case frame を của các động từ, trong đó động từ có dạng liên kết サ変接続名詞. Cải tiến bài tập 46 để thoả mãn các yêu cầu sau đây.

-   Bài tập này tập trung vào các trường hợp một bunsetsu có dạng sau đây liên kết với động từ. 「サ変接続名詞+を（助詞）」

-   Biến đổi các vị ngữ (predicates) về dạng 「サ変接続名詞+を+動詞の基本形」.
    Nếu trong 1 chunk có nhiều động từ, sử dụng động từ bên trái nhất.

-   Trong trường hợp một vĩ ngữ có liên kết với nhiều trợ từ (chunk), in tất cả
    các trợ từ này theo thứ tự từ điển. Các trợ từ cách nhau bởi dấu cách.

-   Trong trường hợp có nhiều chunks liên kết với một vị ngữ (predicate), in tất
    cả các chunk này đồng nhất với thứ tự in của các trợ từ mà nó bao gồm. Các
    chunk được cách nhau bởi ký tự space.

Ví dụ, cho câu sau. 「別段くるにも及ばんさと、主人は手紙に返事をする。」. Chương
trình sẽ in ra kết quả sau.

返事をする と に は 及ばんさと 手紙に 主人は

Lưu kết quả của bài tập 47 ra file, chỉ sử dụng lệnh unix để xác nhận:

- Các vị ngữ (predicates) xuất hiện trong file.

- Các vị ngữ và các case patterns

### 48. Trích xuất ra dependency path từ các danh từ

Chương trình yêu cầu trích xuất ra depedency path của tất cả các chunk có chứa
danh từ từ các chunk đó đến root của cây depedency. Các dependency path phải
thoả mãn yêu cầu sau đây.

-   Biểu diễn các chunk (bunsetsu) dưới dạng chuỗi của các morpheme (surface
    form)

-   Biểu diễn liên kết giữa các bunsetsu bằng ký tự mũi tên (-\>).

Ví dụ, đầu ra cho câu ví dụ 「吾輩はここで始めて人間というものを見た」(câu thứ 8
trong file neko.txt.cabocha) như sau:

吾輩は -\> 見た

ここで -\> 始めて -\> 人間という -\> ものを -\> 見た

人間という -\> ものを -\> 見た

ものを -\> 見た

### 49. Trích xuất ra chuỗi liên kết giữa các danh từ

Trích xuất dependency path ngắn nhất liên kết giữa các noun chunk. Đối với cặp
noun chunk với index tương ứng là *i* và *j* (*i* \< *j*), các dependency paths
thoả mãn các yêu cầu sau. - Giống như bài 48, biểu diễn liên kết giữa các
bunsetsu bằng ký tự mũi tên (-\>). - Thay các noun chunk *i*, và *j* tương ứng
thành X và Y.

Thêm nữa, các dependency path trong bài tập này có thể được diễn dịch như sau. -
Trên đường đi của noun chunk *i* tới gốc của cây, nếu tồn tại noun chunk *j*:
trích xuất dependency path giữa noun chunk *i* và noun chunk *j*. - Ngoài trường
hợp nói trên, nếu đường đi của noun chunk *i* và noun chunk *j* tới gốc của cây
cắt nhau ở bunsetsu *k*: In ra đường đi từ *i* tới bunsetsu ngay trước *k* và
đường đi từ bunsetsu *j* tới bunsetsu ngay trước *k*. Biểu diễn liên kết với
bunsetsu *k* bằng ký tự \|.

Ví dụ, kết quả đưa ra cho câu ví dụ
「吾輩はここで始めて人間というものを見た」(câu thứ 8 trong file
neko.txt.cabocha) như sau:

Xは \| Yで -\> 始めて -\> 人間という -\> ものを \| 見た

Xは \| Yという -\> ものを \| 見た

Xは \| Yを \| 見た

Xで -\> 始めて -\> Y

Xで -\> 始めて -\> 人間という -\> Y

Xという -\> Y

## Chương 6: Xử lý văn bản tiếng Anh

Cài đặt các chương trình xử lý văn bản tiếng Anh
([nlp.txt](<http://www.cl.ecei.tohoku.ac.jp/nlp100/data/nlp.txt>)).

### 50. Tách câu (Sentence segmentation)

Sử dụng patterns (. or ; or : or ? or !) -\> ký tự space -\> chữ cái tiếng Anh
viết hoa (captial letter) để tách các câu trong văn bản. Đầu vào là văn bản
[nlp.txt](<http://www.cl.ecei.tohoku.ac.jp/nlp100/data/nlp.txt>), in ra mỗi câu
trong văn bản trên 1 dòng.

### 51. Tách từ

Coi ký tự trắng (space) là ký tự phân tách các từ. Lấy đầu ra của bài 50 làm đầu
vào, trích xuất các từ trong các câu và in ra theo định dạng: mỗi dòng 1 từ. In
ra dòng trắng để đánh dấu kết thúc câu.

### 52. Stemming

Đầu vào là đầu ra của bài tập 51, áp dụng thuật toán Porter stemming để lấy ra
gốc của các từ (stem). In ra các từ và stem cách nhau bởi ký tự tab. Nếu bạn sử
dụng Python, bạn có thể sử dụng module
[stemming](<https://pypi.python.org/pypi/stemming>).

### 53. Tokenization

Sử dụng tool [Stanford Core
NLP](<http://nlp.stanford.edu/software/corenlp.shtml>) để phân tích văn bản đầu
vào và lấy ra output theo định dạng XML. Sau đó đọc vào đầu ra XML và trích xuất
ra các token (word) theo định dạng mỗi word trên 1 dòng.

### 54. POS Tag

Đọc vào kết quả phân tích dạng XML của Stanford Core NLP. Trích xuất ra word,
lemma, POS tag và in ra các thuộc tính của mỗi word trên một dòng; các thuộc
tính cách nhau bởi dấu tab.

### 55. Trích xuất named entities

Trích xuất tất cả các named entities trong văn bản đầu vào.

### 56. Phân tích coreference

Dựa trên kết quả phân tích coreference của Stanford Core NLP, thay thế các
mention bằng representative mention. Chú ý khi thay thế các mention bằng
representative mention, lưu lại các mention gốc trong dấu ngoặc theo định dạng
representative mention (mention).

### 57. Phân tích cấu trúc dependency

Từ kết quả phân tích dependency của Stanford Core NLP (collapsed-dependencies),
visualize câu đầu vào bằng đồ thị có hướng. Khi visualize các dependency trees,
có thể sử dụng [ngôn ngữ
DOT](<https://en.wikipedia.org/wiki/DOT_%28graph_description_language%29>), hay
sử dụng [Graphviz](<http://www.graphviz.org/>). Nếu sử dụng Python, có thể hiển
thị đồ thị có hướng bằng thư viện/package
[pydot](<https://code.google.com/p/pydot/>).

### 58. Trích xuất tuples

Từ kết quả phân tích dependency của Stanford Core NLP (collapsed-dependencies),
trích xuất các bộ 3 [Subject, Predicate, Purpose] và in ra các bộ 3 này (các
thành phần cách nhau bởi ký tự tab). Subject, Predicate, Purpose được xác định
dựa vào các tiêu chuẩn sau: - Predicate: Là word ở các node con (dependant) của
các dependency relations: nsubj, dobj - Subject: Các node con (dependant) trong
các quan hệ nsubj từ predicate - Purpose: Các node con (dependant) trong các
quan hệ dobj từ predicate

### 59. Phrase structure analysis

Từ kết quả phân tích cây cú pháp phrase structure (theo định dạng
[S-expression](<https://en.wikipedia.org/wiki/S-expression>)), in ra tất cả các
noun phrases trong văn bản. Chú ý, cần in ra cả các noun phrases nằm trong các
noun phrases khác (nested NP).

## Chương 7: Database

File
[artist.json.gz](<http://www.cl.ecei.tohoku.ac.jp/nlp100/data/artist.json.gz>)
là file nén lưu trữ thông tin về các artist trong cơ sở dữ liệu mở
[MusicBrainz](<https://musicbrainz.org/>). Các thông tin về các artist được lưu
trữ ở định dạng JSON, mỗi dòng lưu thông tin về một artist.

Các trường thông tin (field) của file JSON như sau.

| Field                | Nội dung                       | Format                      | Ví dụ                                  |
|----------------------|--------------------------------|-----------------------------|----------------------------------------|
| id                   | id của artist                  | Integer                     | 20660                                  |
| gid                  | global id                      | String                      | "ecf9f3a3-35e9-4c58-acaa-e707fba45060" |
| name                 | Tên artist                     | String                      | "Oasis"                                |
| sort\_name           | Teen artist (dùng để sắp xếp)  | String                      | "Oasis"                                |
| area                 | Khu vực hoạt động              | String                      | "United Kingdom"                       |
| aliases              | Các Tên khác                   | Dictionary                  |                                        |
| aliases[].name       | Tên khác                       | String                      | "Oasis"                                |
| aliases[].sort\_name | Tên khác (dùng để sắp xếp)     | String                      | "Oasis"                                |
| begin                | Ngày bắt đầu hoạt động         | Dictionary                  |                                        |
| begin.year           | Năm bắt đầu hoạt động          | Integer                     | 1991                                   |
| begin.month          | Tháng bắt đầu hoạt động        | Integer                     |                                        |
| begin.date           | Ngày bắt đầu hoạt động         | Integer                     |                                        |
| end                  | Ngày dừng hoạt động            | Dictionary                  |                                        |
| begin.year           | Năm dừng hoạt động             | Integer                     | 2009                                   |
| begin.month          | Tháng dừng đầu hoạt động       | Integer                     |                                        |
| begin.date           | Ngày dừng hoạt động            | Integer                     |                                        |
| tags                 | Tag                            | List các Dictionary objects |                                        |
| tags[].count         | Số tag                         | Integer                     | 1                                      |
| tags[].value         | Nội dung tag                   | String                      | "rock"                                 |
| rating               | Rating                         | Dictionary                  |                                        |
| rating.count         | Số phiếu bình chọn             | Integer                     | 13                                     |
| rating.value         | Giá trị bình chọn (trung bình) | Integer                     | 86                                     |

Hãy suy nghĩ phương pháp lưu trữ, tìm kiếm dữ liệu trong file artist.json.gz
bằng các database [Key-Value-Store
(KVS)](<http://db-engines.com/en/article/Key-value+Stores>) hay
[document-oriented database](<https://www.mongodb.com/document-databases>). Với
KVS database, có thể sử dụng [LevelDB](<http://leveldb.org/>),
[Redis](<http://redis.io/>), [KyotoCabinet](<http://fallabs.com/kyotocabinet/>).
Với document-oriented database, có thể sử dụng
[MongoDB](<http://www.mongodb.org/>), [CouchDB](<http://couchdb.apache.org/>)
hoặc [RethinkDB](<http://rethinkdb.com/>).

### 60. Tạo KVS database

Để giúp cho việc tìm kiếm các trường (fields) từ name đến area của dữ liệu, hãy
sử dụng Key-Value-Store (KVS) để lưu trữ dữ liệu.

### 61. Tìm kiếm với KVS

Sử dụng cơ sở dữ liệu đã tạo ra trong bài tập 60, tìm kiếm khu vực hoạt động
(area) của một artist cho trước.

### 62. Xử lý kiểu vòng lặp trong KVS

Sử dụng cơ sở dữ liệu đã tạo ra trong bài tập 60, hãy đưa ra số artist có khu
vực hoạt động (area) là Japan.

### 63. Lưu trữ các objects (đối tượng) trong KVS

Sử dụng KVS, hãy tạo ra database cho việc tìm kiếm các trường từ name đến tag và
số lượng tag. Thử tìm kiếm các trường từ name đến tag và số lượng tag với
database đã tạo ra.

### 64. Tạo MongoDB

Hãy lưu thông tin của artist (artist.json.gz) vào cơ sở dữ liệu MongoDB. Thêm
nữa, hãy tạo indexes với các trường sau: name, aliases.name, tags.value,
rating.value.

### 65. Tìm kiếm trong cơ sở dữ liệu MongoDB

Sử dụng interactive shell của MongoDB, đưa ra các thông tin liên quan đến artist
có tên "Queen". Tiếp theo, cài đặt chương trình thực hiện chức năng đó.

### 66. Lấy số kết quả tìm kiếm

Sử dụng interactive shell của MongoDB, tính số lượng các artist có khu vực hoạt
động (area) là "Japan."

### 67. Đưa ra multiple documents

Tìm kiếm các artist có aliases cho trước.

### 68. Sắp xếp

Trong số các artist có tag "dance", lấy ra top 10 artist có số phiếu bình chọn
cao nhất.

### 69. Tạo Web application

Tạo ứng dụng Web cho phép người dùng nhập vào các điều kiện tìm kiếm và hiển thị
các artist phù hợp với điều kiện tìm kiếm. Các điều kiện tìm kiếm bao gồm: tên
artist (name), aliases, tag, etc. Hiển thị thông tin các artist (theo dòng) theo
thứ tự từ cao tới thấp của lượng rating.

## Chương 8: Machine Learning

Chương này yêu cầu bạn thực hiện bài toán sentiment analysis trên corpus
[sentence polarity dataset
v1.0](<http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.README.1.0.txt>)
trong [Moview Review
Data](<http://www.cs.cornell.edu/people/pabo/movie-review-data/>) của tác giả Bo
Pang và Lillian Lee. Yêu cầu của bài toán sentiment analysis là phân loại các
câu thành positive và negative sentiments.

### 70. Download và tiền xử lý dữ liệu

Sử dụng dữ liệu liên quan đến sentiment polarity của các câu (download tại
[đây](<http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.tar.gz>)),
tạo dữ liệu chuẩn hoá (sentiment.txt) theo hướng dẫn dưới đây.

1.  Thêm vào '+1' ở bắt đầu các dòng trong file rt-polarity.pos (giữa +1 và nội
    dung của câu cách nhau bởi ký tự trắng).

2.  Thêm vào '-1' ở bắt đầu các dòng trong file rt-polarity.neg (giữa -1 và nội
    dung của câu cách nhau bởi ký tự trắng).

3.  Kết hợp nội dung thu được trong phần 1 và 2 để tạo thành file sentiment.txt

Sau khi đã thu được file sentiment.txt, xác nhận số lượng các câu với positive
polarity và các câu với negative polarity.

### 71. Stopwords

Tạo ra danh sách các stopwords trong tiếng Anh. Sau đó viết 1 hàm để kiểm tra
một từ có thuộc danh sách stopwords hay không. Hàm sẽ trả về giá trị TRUE nếu từ
cho trước thuộc danh sách stopwords. Ngược lại hàm sẽ trả về giá trị FALSE. Sau
đó viết mô tả về các test cho hàm đã viết.

### 72. Trích xuất đặc trưng

Tự thiết kế các đặc trưng cho bài toán sentiment analysis. Sau đó trích xuất đặc
trưng từ dữ liệu training.

Hint: phương pháp trích xuất đặc trưng đơn giản nhất là sử dụng từ gốc (stem)
các từ không trong danh sách các stopwords. Phương pháp này có thể sử dụng để
làm hệ thống baseline.

### 73. Training

Training model bằng phương pháp logistics regressions sử dụng các đặc trưng tạo
ra trong bài 72.

### 74. Prediction

Sử dụng mô hình logistics regressions đã huấn luyện trong bài 73, hãy viết
chương trình dự đoán polarity cho một câu đầu vào và tính xác suất cho các nhãn
(+1, -1).

### 75. Trọng số của các features (Feature weights)

Trong mô hình logistics regression đã huấn luyện trong bài 73, đưa ra top 10 các
features có trọng số cao nhất và top 10 các features có trọng số thấp nhất.

### 76. Dự đoán trên dữ liệu training

Sử dụng mô hình đã học trong bài 73 để đưa ra dự đoán trên dữ liệu training. Đưa
ra nhãn gốc, nhãn dự đoán, và xác suất của nhãn dự đoán cho mỗi câu trong dữ
liệu (cách nhau bởi ký tự tab).

### 77. Tính độ chính xác của mô hình

Sử dụng đầu ra của bài 76, tính accuracy cho toàn bộ dữ liệu; precision, recall,
F1 cho nhãn +1.

### 78. 5-fold cross validation

Vì các thực nghiệm trong bài 76, 77 đánh giá model trên dữ liệu huấn luyện nên
khó có thể nói đó là các đánh giá hợp lý. Các đánh giá này chỉ đánh giá khả năng
mô hình "fit" với dữ liệu training chứ không đánh giá khả năng khái quát
(generalization) của mô hình. Vì thế bài tập 78 yêu cầu bạn đánh giá mô hình sử
dụng 5-fold cross validation. Đưa ra accuracy, precision, recall, F1 score cho
5-fold cross validation (tính trung bình của 5 folds).

### 79. Vẽ đồ thị precision-recall

Vẽ đồ thị precision-recall theo sự thay đổi của giá trị threshold trong mô hình
logistic regression.

## Chương 9: Không gian vector (I)

File
[enwiki-20150112-400-r10-105752.txt.bz2](<http://www.cl.ecei.tohoku.ac.jp/nlp100/data/enwiki-20150112-400-r10-105752.txt.bz2>)
là file nén dạng bzip2 của 105752 file text được lấy mẫu ngẫu nhiên (tỷ lệ 1/10)
từ các bài báo trên Wikipedia có trên 400 từ. Các bài báo trên Wikipedia được
lấy vào ngày 12 tháng 1 năm 2015. Sử dụng dữ liệu file này làm corpus để học các
vector thể hiện ý nghĩa của các từ. Trong nửa đầu của chương 9, bạn được yêu cầu
trích xuất các context của các từ, trích xuất đặc trưng, và dùng phương pháp PCA
để giảm bớt số chiều của dữ liệu. Nửa sau của chương 9 yêu cầu bạn tính độ tương
tự của các từ sử dụng các word vectors đã học từ corpus.

Chú ý, bài 83 yêu cầu 7GB memory. Trong trường hợp lượng memory của bạn không
đủ, bạn cần có các phương pháp xử lý thích hợp hoặc sử dụng sample 1/100 của dữ
liệu trong file
[enwiki-20150112-400-r10-105752.txt.bz2](<http://www.cl.ecei.tohoku.ac.jp/nlp100/data/enwiki-20150112-400-r10-105752.txt.bz2>).

### 80. Tiền xử lý dữ liệu

Sử dụng khoảng trắng là ký tự ngăn cách để tokenize các từ trong các câu. Phương
pháp này có nhược điểm là các từ thu được sẽ còn các ký tự đặc biệt như dấu câu,
hoặc dấu ngoặc. Vì thế sau khi tokenize các từ trong corpus, tiến hành các xử lý
sau đây. 

- Xoá các ký tự đặc biệt xuất hiện ở đầu và cuối các từ: .,!?;:()[]'" 
- Xoá các từ chỉ gồm ký tự trắng

Sau khi tiền xử lý dữ liệu, lưu file dữ liệu gồm danh sách các từ cách nhau bởi
khoảng trắng.

### 81. Xử lý tên các nước tạo thành từ các compound words

Trong tiếng Anh, nhiều từ cạnh nhau có thể tạo thành một từ có ý nghĩa. Ví dụ,
hợp chủng quốc Hoa Kỳ là "United States", vương quốc Anh là "United Kingdom".
Nếu chỉ dùng các "United", "State", hay "Kingdom" như các từ riêng lẻ, ý nghĩa
của các từ này sẽ nhập nhằng. Vì thế trong khi tiền xử lý dữ liệu, ta cần xác
định các từ ghép này. Đoán nhận các từ ghép là một bài toán khó, nên ở đây ta
chỉ đoán nhận các từ ghép là tên của các nước.

Trước hết, download danh sách tên của các nước trên Internet. Dùng danh sách tên
các nước này để đoán nhận các từ ghép là tên nước trong dữ liệu sử dụng ở bài
80, sau đó biến đổi các ký tự spaces thành ký tự underscore (\_) để nối các từ
thành phần. Ví dụ "United States" sẽ trở thành "United\_States", "Isle of Man"
sẽ trở thành "Isle\_of\_Man."

### 82. Trích xuất context

Sử dụng corpus được tạo ra trong bài tập 81, trích xuất context của tất cả các
từ xuất hiện trong corpus. Context của mỗi từ *t* trong dữ liệu sẽ cặp với từ
*t* và xuất ra theo định dạng: các thông tin cách nhau bởi ký tự tab. Context
của mỗi từ *t* được định nghĩa như sau: 

- Trích xuất các từ ở trước và sau của
*t* với kích thước cửa sổ là *d* (chú ý context words của *t* sẽ không bao gồm
bản thân của từ *t*) 
- Với mỗi từ *t*, kích thước của context (window size) *d*
sẽ được chọn ngẫu nhiên trong tập {1, 2, 3, 4, 5}.

### 83. Tính tần xuất xuất hiện của từ/context

Sử dụng đầu ra của bài 82, tính phân bố xuất hiện và các hằng số sau: 

- *f*(*t*,*c*): là số lần đồng xuất hiện của từ *t* và context word *c*.
- *f*(*t*,\*): số lần xuất hiện của từ *t*.
- *f*(\*,*c*): số lần xuất hiện của context word *c*.
- *N*: Tổng số lần xuất hiện của từ và các context word (hằng số).

### 84. Tạo Matrix của các từ và context words

Sử dụng đầu ra của bài 83, tạo ma trận word/context *X*. Các thành phần X\_tc
trong ma trận *X* được định nghĩa như sau. - Nếu *f*(*t*,*c*) \>= 10, X\_tc =
PPMI(t,c) = max{log N\*f(t,c)/f(t,\*) x f(\*,c),0} - Nếu f(t,c) \< 10, X\_tc =
0.

Ở đây PPMI(t,c) là ký hiệu của Pointwise Mutual Information. Chú ý vì kích thước
ma trận X là rất lớn, nên lưu tất cả các giá trị của ma trận vào bộ nhớ là không
thể. Bạn có thể sử dụng kỹ thuật lưu trữ ma trận thưa với chú ý rằng, phần lớn
giá trị của các phần tử trong X bằng 0.

### 85. Sử dụng PCA để giảm số chiều dữ liệu

Sử dụng thuật toán PCA cho ma trận thu được trong bài tập 84 để giảm số chiều dữ
liệu sao cho các word vector thu được có số chiều là 300.

### 86. Hiển thị word vectors

Đọc vào các word vectors trong bài tập 85, hiển thị vector cho từ "United
States". Chú ý là từ "United States" trong corpus đã được biến đổi thành
"United\_States."

### 87. Tính word similarity

Sử dụng word vectors thu được trong bài tập 85, tính cosine similarity cho hai
từ "United States" và "U.S." Chú ý là từ "U.S." trong corpus được lưu trữ là
"U.S"

### 88. Hiển thị top 10 có giá trị similarity cao nhất

Sử dụng word vectors trong bài 85, hiển thị top 10 từ với cosine similarity cao
nhất với từ "England" và các giá trị cosine similarity tương ứng.

### 89. Các thao tác cộng/trừ word vectors

Đọc vào các word vectors thu được trong bài 85, tính vec("Spain") -
vec("Madrid") + vec("Athens") sau đó hiển thị top 10 từ có cosine similarity gần
nhất với vector thu được cùng với các giá trị cosine similarity tương ứng.

## Chương 10: Không gian vector (II)

Trong chương 10, chúng ta sẽ tiếp tục nội dung của chương 9 về không gian
vector.

### 90. Sử dụng word2vec để học word vectors

Áp dụng [word2vec](<https://code.google.com/p/word2vec/>) trên corpus đã tạo ra
ở bài 81 để học word vectors. Sau đó, sử dụng các word vectors đã học với
word2vec để áp dụng cho các bài tập 86-89.

### 91. Chuẩn bị dữ liệu analogy

Download dữ liệu [analogy
evaluation](<https://word2vec.googlecode.com/svn/trunk/questions-words.txt>).
Trong dữ liệu, các dòng bắt đầu bằng ":" thể hiện tên của section. Ví dụ dòng ":
capital-common-countries" bắt đầu cho section "capital-common-countries." Hãy
trích xuất các dòng của section "family" trong file đã download và lưu ra file.

### 92. Vận dụng dữ liệu analogy data

Với các dòng trong dữ liệu analogy tạo ra trong bài 91, tính vector sau:
vec(word ở cột 2) - vec(word ở cột 1) + vec(word ở cột 3) sau đó tìm word với
word vector với độ tương tự cao nhất với word vector đã tính đồng thời tính độ
tương tự (cosine similarity). Thêm vào cuối của các dòng từ tìm được và độ tương
tự. Trong bài tập này, hãy thử sử dụng word vector đã học được sau bài 85 và bài
90.

### 93. Tính độ chính xác của mô hình trên dữ liệu analogy

Sử dụng dữ liệu của bài 92, tính độ chính xác của các mô hình với mô hình
analogy.

### 94. Tính word similarity trên dữ liệu WordSimilarity-353

Sử dụng đầu vào là dữ liệu [The WordSimilarity-353 Test
Collection](<http://www.cs.technion.ac.il/~gabr/resources/data/wordsim353/>),
tính độ tương tự của các từ ở cột 1 và cột 2 và thêm vào cuối các dòng giá trị
độ tương tự này. Hãy áp dụng các mô hình word vectors đã học ở bài 85 và bài 90.

### 95. Đánh giá trên dữ liệu WordSimilarity-353

Sử dụng dữ liệu trong bài 94, sử dụng ranking với các giá trị độ tương tự đã
tính với các mô hình và ranking do con người đưa ra để tính [Spearman
correlation](<https://en.wikipedia.org/wiki/Spearman's_rank_correlation_coefficient>).

### 96. Trích xuất vectors liên quan đến tên nước

Sử dụng mô hình đã học với word2vec, trích xuất các vectors của các từ liên quan
đến tên các nước.

### 97. k-means clustering

Lấy đầu vào là các word vectors từ bài tập 96, thực hiện clustering bằng thuật
toán k-means với số lượng clusters *k* = 5.

### 98. Clustering với phương pháp Ward

Lấy đầu vào là các word vectors từ bài tập 96 (các word vectors của tên các
nước), thực hiện hierarchical clustering bằng [phương pháp
Ward](<https://en.wikipedia.org/wiki/Ward's_method>). Sau đó, visualize kết quả
clustering bằng [dendrogram](<https://en.wikipedia.org/wiki/Dendrogram>).

### 99. Visualize word vectors bằng phương pháp t-SNE

Với các word vectors thu được từ bài tập 96, visualize không gian vectors bằng
[phương pháp t-SNE](<http://www.jmlr.org/papers/v9/vandermaaten08a.html>).

## Phụ lục: Corpus, data sử dụng trong 100 bài luyện tập NLP

-   [hightemp.txt](<http://www.cl.ecei.tohoku.ac.jp/nlp100/data/hightemp.txt>):
    Dữ liệu nhiệt độ cao nhất ở các địa phương qua các thời kỳ do nha khí tượng
    Nhật Bản cung cấp.

-   [jawiki-country.json.gz](<http://www.cl.ecei.tohoku.ac.jp/nlp100/data/jawiki-country.json.gz>):
    Dữ liệu Wikipedia tiếng Nhật gồm các bài báo (trong ngày 18/10/2014) về các
    quốc gia, được trích xuất từ [Wikipedia Dump data (tiếng
    Nhật)](<http://dumps.wikimedia.org/jawiki/latest/jawiki-latest-pages-articles.xml.bz2>).
    Dữ liệu được lưu trữ bằng định dạng JSON.

-   [neko.txt](<http://www.cl.ecei.tohoku.ac.jp/nlp100/data/neko.txt>): là nội
    dung bằng plain text của cuốn tiểu thuyết "吾輩は猫である" của nhà văn
    夏目漱石 (Soseki Natsume) được cung cấp miễn phí tại trang Web:
    [青空文庫](<http://www.aozora.gr.jp/>).

-   [nlp.txt](<http://www.cl.ecei.tohoku.ac.jp/nlp100/data/nlp.txt>): nội dung
    của trang Wikipedia nói về [Natural Language
    Processing](<https://en.wikipedia.org/wiki/Natural_language_processing>) với
    định dạng 1 dòng 1 câu.

-   [artist.json.gz](<http://www.cl.ecei.tohoku.ac.jp/nlp100/data/artist.json.gz>):
    là file nén lưu trữ thông tin về các artist trong cơ sở dữ liệu mở
    [MusicBrainz](<https://musicbrainz.org/>). Các thông tin về các artist được
    lưu trữ ở định dạng JSON, mỗi dòng lưu thông tin về một artist.

-   [enwiki-20150112-400-r10-105752.txt.bz2](<http://www.cl.ecei.tohoku.ac.jp/nlp100/data/enwiki-20150112-400-r10-105752.txt.bz2>)
    là file nén dạng bzip2 của 105752 file text được lấy mẫu ngẫu nhiên (tỷ lệ
    1/10) từ các bài báo trên Wikipedia có trên 400 từ. Các bài báo trên
    Wikipedia được lấy vào ngày 12 tháng 1 năm 2015.
