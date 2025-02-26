total_land_area=80
plot_size=total_land_area/5

tomato_yield=((0.3*plot_size)*10*1000)+((0.3*plot_size)*12*1000)
tomato_revenue=7*tomato_yield
potato_yield=10*plot_size*1000
potato_revenue=potato_yield*20
cabbage_yield=14*plot_size*1000
cabbage_revenue=cabbage_yield*24
sunflower_yield=0.7*plot_size*1000
sunflower_revenue=sunflower_yield*200
sugarcane_yield=45*plot_size
sugarcane_revenue=sugarcane_yield*4000

total_revenue=tomato_revenue+potato_revenue+cabbage_revenue+sugarcane_revenue+sunflower_revenue
chemical_free_revenue=total_revenue-sugarcane_revenue

print("Total Revenue:",total_revenue)
print("Chemical-Free Revenue:",chemical_free_revenue)
