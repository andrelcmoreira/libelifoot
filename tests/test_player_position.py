from libelifoot.util.player_position import PlayerPosition


def test_to_pos_code_with_unknown_pos_str():
    ret = PlayerPosition.to_pos_code("unknown")

    assert ret == PlayerPosition.U.value


def test_to_pos_code_with_gk_pos_str():
    ret = PlayerPosition.to_pos_code("G")

    assert ret == PlayerPosition.G.value


def test_to_pos_code_with_df_pos_str():
    ret = PlayerPosition.to_pos_code("D")

    assert ret == PlayerPosition.D.value


def test_to_pos_code_with_mf_pos_str():
    ret = PlayerPosition.to_pos_code("M")

    assert ret == PlayerPosition.M.value


def test_to_pos_code_with_fw_pos_str():
    ret = PlayerPosition.to_pos_code("A")

    assert ret == PlayerPosition.A.value


def test_to_pos_code_with_unknown_pos_code():
    ret = PlayerPosition.to_pos_name(123)

    assert ret == PlayerPosition.U.name


def test_to_pos_code_with_gk_pos_code():
    ret = PlayerPosition.to_pos_name(PlayerPosition.G.value)

    assert ret == PlayerPosition.G.name


def test_to_pos_code_with_df_pos_code():
    ret = PlayerPosition.to_pos_name(PlayerPosition.D.value)

    assert ret == PlayerPosition.D.name


def test_to_pos_code_with_mf_pos_code():
    ret = PlayerPosition.to_pos_name(PlayerPosition.M.value)

    assert ret == PlayerPosition.M.name


def test_to_pos_code_with_fw_pos_code():
    ret = PlayerPosition.to_pos_name(PlayerPosition.A.value)

    assert ret == PlayerPosition.A.name
