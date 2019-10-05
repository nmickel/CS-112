print('Welcome to the Cake Slice Program!')
cake=input('What kind of cake did you make? ')
length=int(input('How long is the cake in centimeters? '))
wide=int(input('How wide is the cake in centimeters? '))
length_slice=int(input('How long will you cut your slices in centimeters? '))
wide_slice=int(input('How wide will you cut your slices in centimeters? '))
surface_area=length*wide; # find the surface area by multiplying length x width
print('Your cake has a surface area of %s square centimeters.' % surface_area)
pieces=(length//length_slice)*(wide//wide_slice)
print('You can cut %s total %sx%s slices of cake.' % (pieces, length_slice, wide_slice))
consume_area=pieces*length_slice*wide_slice
percent = int(consume_area/surface_area*100)
print('These slice dimensions can cut a total of %s square centimeters, or %s%%, of the cake.' % (consume_area, percent))
wasted_area=surface_area-consume_area
wasted_percentage=round((1-consume_area/surface_area)*100)
print('These slice dimensions will waste %s square centimeters, or %s%%, of the cake.' % (wasted_area, wasted_percentage))
utilised_length=(length//length_slice)*length_slice
utilised_width=(wide//wide_slice)*wide_slice
centered_pieces=(utilised_length-2*length_slice)*(utilised_width-2*wide_slice)
edge_pieces=pieces-centered_pieces
print('There will be %s edge pieces, and %s center pieces of cake.' % (edge_pieces, centered_pieces ))
print('Enjoy your %s cake!' % cake)