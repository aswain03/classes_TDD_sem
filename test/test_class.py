from src.player_class import Create_player


class TestProperties:

    def test_default_name_property(self):
        player = Create_player()
        assert player.name == "Tav"

    def test_name_property(self):
        player = Create_player("Frungus")
        assert player.name == "Frungus"

    def test_stats_property(self):
        player = Create_player("Frungus")
        assert player.stats == {}

    def test_inventory_property(self):
        player = Create_player("Frungus")
        assert player.backpack == []

    def test_capacity_property(self):
        player = Create_player("Frungus")
        assert player.capacity == 10

    def test_level_property(self):
        player = Create_player("Frungus")
        assert player.level == 1


class TestMethods:

    def test_add_stats(self):
        player = Create_player("Frungus")
        player.add_stats("strength", 3)
        assert player.stats == {"strength": 3}
        assert player.add_stats("strength", 3) == "3 points added to strength"

    def test_add_multiple_stats(self):
        player = Create_player("Frungus")
        player.add_stats("strength", 3)
        player.add_stats("agility", 2)
        assert player.stats == {"strength": 3, "agility": 2}
        assert player.add_stats("agility", 2) == "2 points added to agility"
        assert player.add_stats("strength", 3) == "3 points added to strength"

    def test_add_to_backpack(self):
        player = Create_player("Frungus")
        player.add_to_backpack("sword")
        assert player.backpack == ["sword"]
        assert player.add_to_backpack("sword") == "sword added to backpack"

    def test_backpack_capacity(self):
        player = Create_player("Frungus")
        for i in range(10):
            player.add_to_backpack("sword")
        assert player.add_to_backpack("sword") == "Backpack is full"
        assert player.backpack == ["sword"] * 10
        assert player.capacity == 10

    def test_backpack_capacity_with_different_items(self):
        player = Create_player("Frungus")
        for i in range(5):
            player.add_to_backpack("sword")
            player.add_to_backpack("shield")
        assert player.add_to_backpack("sword") == "Backpack is full"
        assert player.backpack == ["sword", "shield"] * 5
        assert player.capacity == 10

    def test_increase_backpack_capacity(self):
        player = Create_player("Frungus")
        player.increase_backpack_capacity(5)
        assert player.capacity == 15
        assert (
            player.increase_backpack_capacity(5)
            == "Backpack capacity increased by 5"
        )

    def test_level_up(self):
        player = Create_player("Frungus")
        player.add_stats("strength", 3)
        player.level_up("strength")

        assert player.level == 2
        assert player.stats == {"strength": 8}
        assert (
            player.level_up("strength")
            == "You leveled up! strength increased by 5 points"
        )

    def test_show_backpack(self):
        player = Create_player("Frungus")
        player.add_to_backpack("sword")
        player.add_to_backpack("shield")
        assert player.show_backpack() == ["sword", "shield"]
