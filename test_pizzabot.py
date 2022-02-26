import unittest


from pizzabot import (
	validate_grid_points_format,
	validate_grid_point_limits,
	Pizzabot
	)


class TestSum(unittest.TestCase):

	def test_validate_grid_points_format(self):
		valid_input = '5x5(1,3)(4,4)(2,3)'
		invalid_input = '5x(1,3)(4,4)(2,3)'
		with self.assertRaises(SystemExit) as SE:
		    validate_grid_points_format(invalid_input)

		self.assertEqual(SE.exception.code, 'invalid format')

		assert validate_grid_points_format(valid_input) == None
		

	def test_validate_grid_point_limits(self):
		m, n = 4,5
		target_out_limits = (3,9)
		target_in_limits = (2,1)
		with self.assertRaises(SystemExit) as SE:
		    validate_grid_point_limits(m, n, target_out_limits)

		self.assertEqual(SE.exception.code, 'House is out of my limits')
		
		assert validate_grid_point_limits(m, n, target_in_limits) == None


	def test_bot_mouvement(self):
		bot = Pizzabot(0, 0)
		points_test = [(1, 3), (4, 4)]
		
		for point in points_test:
			bot.move_to_point(point)

		
		self.assertEqual(''.join(bot.mouvements), 'ENNNDEEEND')
		

if __name__ == "__main__":
	unittest.main()
