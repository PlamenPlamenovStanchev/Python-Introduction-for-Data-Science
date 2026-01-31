from math import ceil, floor

CAN_OF_PAINT_PRICE = 21.50
WALL_PAPER_ROLL_PRICE = 5.20


paint_cans_count = int(input())
wall_paper_rolls_count = int(input())
pair_of_gloves_price = float(input())
brush_price = float(input())


total_paint_cost = paint_cans_count * CAN_OF_PAINT_PRICE
total_wall_paper_cost = wall_paper_rolls_count * WALL_PAPER_ROLL_PRICE
gloves_required = ceil(wall_paper_rolls_count * 0.35)
required_brushes = floor(paint_cans_count * 0.48)

total_price_for_gloves = gloves_required * pair_of_gloves_price
total_price_for_brushes = required_brushes * brush_price
total_price_of_all_materials = (
    total_paint_cost +
    total_wall_paper_cost +
    total_price_for_gloves +
    total_price_for_brushes
)
delivery_cost = total_price_of_all_materials / 15


print(f"This delivery will cost {delivery_cost:.2f} lv." )