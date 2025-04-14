CREATE TABLE sup (
    Sid INT AUTO_INCREMENT PRIMARY KEY,  -- 供应商ID，自动递增主键
    Sname VARCHAR(100) NOT NULL,         -- 供应商名称，字符串，必填
    Sadd VARCHAR(255),                   -- 供应商地址，字符串，可选
    phone VARCHAR(20)
                     -- 供应商电话，字符串，可选
);

CREATE TABLE mat (
    Mid INT AUTO_INCREMENT PRIMARY KEY,  -- 物品ID，自动递增主键
    Mname VARCHAR(100) NOT NULL,         -- 物品名称，字符串，必填
    Mprice DECIMAL(10, 2) NOT NULL,      -- 物品价格，10位数字，精确到小数点后两位
    Mnum INT NOT NULL                     -- 数量，整数，必填
);

CREATE TABLE win (
    Wid INT AUTO_INCREMENT PRIMARY KEY,  -- 窗口ID，自动递增主键
    Wadd VARCHAR(255) NOT NULL,          -- 窗口地址，字符串，必填
    time DATETIME NOT NULL,              -- 操作时间，日期时间类型，必填
    cate VARCHAR(100),                   -- 分类，字符串，可选
    Wremark INT                      -- 备注，文本类型，可选
);

CREATE TABLE cook (
    Cid INT AUTO_INCREMENT PRIMARY KEY,  -- 厨师ID，自动递增主键
    Cname VARCHAR(100) NOT NULL,         -- 厨师名称，字符串，必填
    Wid INT NOT NULL,                    -- 窗口ID，外键，必填
    FOREIGN KEY (Wid) REFERENCES win(Wid) -- 设置Wid为外键，引用win表的Wid
);

CREATE TABLE veg (
    Vid INT AUTO_INCREMENT PRIMARY KEY, -- 菜品ID，主键，自增
    Vname VARCHAR(255) NOT NULL,        -- 菜品名称
    Vprice DECIMAL(10, 2) NOT NULL,     -- 菜品价格，精确到小数点后两位
    sale INT DEFAULT 0,                 -- 销售数量，默认值为0
    Vremark INT                   -- 菜品备注，可为空
);

CREATE TABLE buy (
    Bid INT PRIMARY KEY,
    Bname VARCHAR(255) NOT NULL,
    money DECIMAL(10, 2) NOT NULL
);

-- 关系

CREATE TABLE reg (                    -- 供应商ID，外键，必填
    Wid INT NOT NULL,-- 窗口ID，外键，必填
    Sid INT NOT NULL,
    Rnum INT NOT NULL,                   -- 进货数量，必填
    PRIMARY KEY (Sid, Wid),              -- Sid 和 Wid 作为复合主键
    FOREIGN KEY (Sid) REFERENCES sup(SID), -- 设置Sid为外键，引用sup表的Sid
    FOREIGN KEY (Wid) REFERENCES win(Wid)  -- 设置Wid为外键，引用win表的Wid
);

CREATE TABLE hav (
    Sid INT NOT NULL,                    -- 供应商ID，外键，必填
    Mid INT NOT NULL,                    -- 窗口ID，外键，必填
    PRIMARY KEY (Sid, Mid),              -- Sid 和 Wid 作为复合主键
    FOREIGN KEY (Sid) REFERENCES sup(SID), -- 设置Sid为外键，引用sup表的Sid
    FOREIGN KEY (Mid) REFERENCES mat(Mid)  -- 设置Wid为外键，引用win表的Wid
);

CREATE TABLE whv (
    Wid INT NOT NULL,                    -- 供应商ID，外键，必填
    Vid INT NOT NULL,                    -- 窗口ID，外键，必填
    PRIMARY KEY (Wid, Vid),              -- Sid 和 Wid 作为复合主键
    FOREIGN KEY (Wid) REFERENCES win(Wid) , -- 设置Sid为外键，引用sup表的Sid
    FOREIGN KEY (Vid) REFERENCES veg(Vid)  -- 设置Wid为外键，引用win表的Wid
);

-- ---------------------------------------------------


CREATE TABLE cmv (
    Cid INT NOT NULL,                    -- 供应商ID，外键，必填
    Vid INT NOT NULL,                    -- 窗口ID，外键，必填
    PRIMARY KEY (Cid, Vid),              -- Sid 和 Wid 作为复合主键
    FOREIGN KEY (Cid) REFERENCES cook(Cid), -- 设置Sid为外键，引用sup表的Sid
    FOREIGN KEY (Vid) REFERENCES veg(Vid)  -- 设置Wid为外键，引用win表的Wid
);

CREATE TABLE bbv (
    Bid INT NOT NULL,                    -- 供应商ID，外键，必填
    Vid INT NOT NULL,                    -- 窗口ID，外键，必填
    Bnum INT NOT NULL,
    PRIMARY KEY (Bid, Vid),              -- Sid 和 Wid 作为复合主键
    FOREIGN KEY (Bid) REFERENCES buy(Bid), -- 设置Sid为外键，引用sup表的Sid
    FOREIGN KEY (Vid) REFERENCES veg(vid)  -- 设置Wid为外键，引用win表的Wid
);

ALTER TABLE bbv DROP FOREIGN KEY bbv_ibfk_1;
ALTER TABLE bbv DROP FOREIGN KEY bbv_ibfk_2;

ALTER TABLE bbv
ADD COLUMN Btime DATETIME NOT NULL; -- 添加 Btime 列，类型为 DATETIME


ALTER TABLE bbv
DROP PRIMARY KEY,
ADD PRIMARY KEY (Bid, Vid, Btime);
ALTER TABLE bbv
ADD CONSTRAINT bbv_ibfk_1 FOREIGN KEY (Bid) REFERENCES buy (Bid),
ADD CONSTRAINT bbv_ibfk_2 FOREIGN KEY (Vid) REFERENCES veg (Vid);



DROP TABLE IF EXISTS cmv;
DROP TABLE IF EXISTS whv;
DROP TABLE IF EXISTS hav;
DROP TABLE IF EXISTS reg;
DROP TABLE IF EXISTS bbv;
DROP TABLE IF EXISTS buy;
DROP TABLE IF EXISTS veg;
DROP TABLE IF EXISTS cook;
DROP TABLE IF EXISTS win;
DROP TABLE IF EXISTS mat;
DROP TABLE IF EXISTS sup;