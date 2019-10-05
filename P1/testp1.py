print('"Welcome to the Cake Slice Program!"')
cake=input('"What Kind of cake did you make?"')
length=int(input('"How long is the cake in centimeters?"'))
wide=int(input('"How wide is the cake in centimeters?"'))
length_slice=int(input('"How long will you cut your slices in centimeters?"'))
wide_slice=int(input('"How wide will you cut your slices in centimeters?"'))
surface_area=length*wide;
print('surface area=',surface_area);
pieces=(length//length_slice)*(wide//wide_slice)
print('Number of pieces that can be cut:',pieces)
consume_area=pieces*length_slice*wide_slice;
print('consumption percentage=',consume_area/surface_area*100)
print('wastage percentage=',(1-consume_area/surface_area)*100)
utilised_length=(length//length_slice)*length_slice
utilised_width=(wide//wide_slice)*wide_slice
centered_pieces=(utilised_length-2*length_slice)*(utilised_width-2*wide_slice)
edge_pieces=pieces-centered_pieces
print('There will be %s edge pieces, and %s center pieces of cake' % (edge_pieces, centered_pieces))