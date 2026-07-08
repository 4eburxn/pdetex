function Math(elem)
  -- Проверяем, является ли формула инлайн и содержит ли она \displaystyle
  if elem.mathtype == 'InlineMath' and elem.text:find('\\displaystyle') then
    -- Превращаем её в выключную формулу (DisplayMath)
    return pandoc.Math('DisplayMath', elem.text)
  end
end
