Jekyll::Hooks.register :pages, :post_init do |page|

  # get the current post last modified time
  modification_time = File.mtime( page.path )
  
  # inject modification_time in post's datas.
  page.data['last-modified-date'] = modification_time
  
end