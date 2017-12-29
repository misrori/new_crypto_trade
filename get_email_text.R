library(rvest)
library(data.table  )
get_coin_list <- function(exc) {
  nev <- strsplit(exc, '/')[[1]][3]
  my_link <- paste0('https://coinmarketcap.com', exc)
  t <- read_html(my_link)%>%
    html_table()
  
  return(data.table('market'= nev, 'coin'= unique(t[[1]]$Currency)))
}

#####
# top_50_market <- function(){
#   linkek <- read_html('https://coinmarketcap.com/exchanges/volume/24-hour/all/')%>%
#     html_nodes('.volume-header a')%>%
#     html_attr('href')
#     linkek <- linkek[1:50]
# }
# markets <- top_50_market()
# 
# 
# fileConn<-file("markets.txt")
# writeLines(paste(markets, collapse = ","), fileConn)
# close(fileConn)
#####
con <- file("/home/mihaly/R_codes/new_crypto_trade/markets.txt")
markets <- strsplit(readLines(con = con), ',')[[1]]
close(con)


fileConn<-file("/home/mihaly/R_codes/new_crypto_trade/uj_coins.txt", 'w')
writeLines("", fileConn)
close(fileConn)

regi_adat <- fread('/home/mihaly/R_codes/new_crypto_trade/coinok_lista.csv')

coinok <- lapply(markets, get_coin_list) 

eredmeny <- rbindlist(coinok)
eredmeny$coinname <- paste0(eredmeny$coin,'#', eredmeny$market)


if(length(eredmeny[coinname%in%regi_adat$coinname==F,]$coinname)!=0){
  fileConn<-file("/home/mihaly/R_codes/new_crypto_trade/uj_coins.txt")
  writeLines(paste(eredmeny[coinname%in%regi_adat$coinname==F,]$coinname, collapse = "\n"), fileConn)
  close(fileConn)
  system( '/home/mihaly/hadoop/anaconda3/bin/python /home/mihaly/R_codes/new_crypto_trade/new_trade.py' )
  
  
}

write.csv(eredmeny, "/home/mihaly/R_codes/new_crypto_trade/coinok_lista.csv", row.names = F)
print(Sys.time())





